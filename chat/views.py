from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Chat
from .models import Message
from .models import Access
from .utils import get_chats
from .utils import generate_chat
from .utils import get_chat_messages
from .utils import send_message
from .utils import get_dialog
from .utils import chat_access
from .utils import get_chat_members
from .utils import give_or_save_access
from .utils import ignore_or_refuse_access
from .utils import leave_chat as leave_chat_util
from .utils import normalize_chat_member
from .forms import MessageForm
from users.utils import get_user
from users.utils import get_profile
from users.utils import get_friends
from users.models import User
# Create your views here.


@login_required
def chat_list(request):
    def clear(chats):
        for chat in chats:
            print(chat)
            if chat['last_message'] is not None:
                yield chat

    context = {}

    chats_objects = get_chats(request.user)

    chats = [generate_chat(chat, request.user)
             for chat
             in chats_objects]

    context['chats'] = clear(chats)

    return render(request, 'chatlist.html', context)


@login_required
def chat_page(request, id):
    context = {}

    try:
        chat = Chat.objects.get(id=id)
    except Chat.DoesNotExist:
        return redirect('chatlist')

    try:
        access = Access.objects.get(user=request.user, chat=chat)
        if access.mode == 0:
            return redirect('chatlist')
    except Access.DoesNotExist:
        return redirect('chatlist')

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            print(chat)
            print(request.user)
            print(message_form.data['content'])
            send_message(chat, request.user, message_form.data['content'])

            context['message_form'] = MessageForm()
        else:
            context['message_form'] = message_form
    else:
        context['message_form'] = MessageForm()
    messages = get_chat_messages(chat, request.user)
    chat = generate_chat(chat, request.user)
    context['chat'] = chat
    context['messages'] = messages

    return render(request, 'chat.html', context)


@login_required
def open_dialog(request, interlocutor_id):
    try:
        interlocutor = get_user(interlocutor_id)
        me = request.user
    except User.DoesNotExist:
        return redirect('home')
    else:
        dialog = get_dialog(me, interlocutor)
        return redirect(reverse('chat', args=[dialog.id]))


@login_required
def multichat_info(request, chat_id):
    access = chat_access(request.user.id, chat_id)
    if not access:
        return redirect(reverse('multychat-info', args=[chat_id]))

    access_mode = access.mode
    chat = access.chat

    if access_mode in [3, 4]:
        # return multichat_settings(request, chat_id)
        pass

    context = {}
    context['chat_id'] = chat_id
    context['chat_name'] = chat.name

    context['members'] = [normalize_chat_member(access)
                          for access
                          in Access.objects.filter(chat=chat, mode__in=[1, 2, 3, 4])]
    context['banned'] = [normalize_chat_member(access)
                         for access
                         in Access.objects.filter(chat=chat, mode=0)]

    context['members_count'] = len(context['members'])
    context['banned_count'] = len(context['banned'])

    return render(request, 'multychat_info.html', context)


@login_required
def multichat_settings(request, chat_id):
    access = chat_access(request.user.id, chat_id)
    if not access or access.mode not in [2, 3, 4]:
        print('denied')
        return redirect(reverse('multychat-info', args=[chat_id]))

    access_mode = access.mode
    chat = access.chat
    context = {}
    context['chat_id'] = chat_id

    if request.method == 'POST':
        print(request.POST)
        print('POST request for chat settings')

        accepted_members = dict(request.POST)['members-checkbox-form']
        accepted_members = list(map(int, accepted_members))

        members = [access.user
                   for access
                   in Access.objects.filter(chat=chat)]

        invitable = [friend
                     for friend
                     in get_friends(access.user)
                     if friend not in members]

        members.extend(invitable)

        for member in members:
            if member.id in accepted_members:
                give_or_save_access(member, chat)
            else:
                ignore_or_refuse_access(member, chat)

        new_chat_name = dict(request.POST)['chat-name-form'][0]
        if new_chat_name:
            chat.name = new_chat_name
            chat.save()
        return redirect(reverse('multychat-info', args=[chat_id]))
    if request.method == 'PUT':
        print(request.PUT)
        return redirect(reverse('multychat-info', args=[chat_id]))
    if request.method == 'GET':

        context['members'] = [get_profile(access.user)
                              for access
                              in Access.objects.filter(chat=chat, mode__in=[1, 2, 3, 4])]
        context['banned'] = [get_profile(access.user)
                             for access
                             in Access.objects.filter(chat=chat, mode=0)]

        context['invitable'] = [get_profile(friend)
                                for friend
                                in get_friends(access.user)
                                if get_profile(friend) not in context['members']
                                and get_profile(friend) not in context['banned']]

        context['chat_name'] = chat.name
        return render(request, 'multychat_settings.html', context)


@login_required
def leave_chat(request, chat_id):
    access = chat_access(request.user.id, chat_id)
    print(access.chat)
    if access:
        leave_chat_util(access.user, access.chat)
    return redirect('chat-list')


def new_multychat(request):
    chat = Chat(is_multy=True, name="Untitled")
    chat.save()
    access = Access(user=request.user, chat=chat, mode=4)
    access.save()
    message = Message(chat=chat, author=request.user,
                      content="У меня право на первое сообщение на уровне сервера хахаха")
    message.save()
    return redirect('chat-list')
