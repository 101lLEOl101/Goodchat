from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Chat
from .models import Message
from .models import Access
from .utils import generate_chat
from .utils import get_chat_messages
from users.models import Profile
# Create your views here.


@login_required(login_url='login')
def chat_list(request):
    try:
        profile = Profile.objects.get(id=request.user.id)
    except Profile.DoesNotExist:
        return redirect('home')
    context = {
        'profile': {
            'id': request.user.id,
            'avatar': profile.avatar,
        }
    }
    context['user'] = request.user

    chats_objects = [access.chat
                     for access
                     in Access.objects.filter(user=request.user)]

    chats = [generate_chat(chat, request.user)
             for chat
             in chats_objects]

    context['chats'] = chats

    return render(request, 'chatlist.html', context)

def chat_page(request, id):
    try:
        profile = Profile.objects.get(id=request.user.id)
    except Profile.DoesNotExist:
        return redirect('home')
    context = {
        'profile': {
            'id': request.user.id,
            'avatar': profile.avatar,
        }
    }
    
    try:
        chat = Chat.objects.get(id=id)
    except Chat.DoesNotExist:
        return redirect('chatlist')
    
    messages = get_chat_messages(chat, request.user)
    chat = generate_chat(chat, request.user)
    context['chat'] = chat
    context['messages'] = messages
    
    
    return render(request, 'chat.html', context)
