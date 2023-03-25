from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat
from .models import Message
from .models import Access
from .utils import generate_chat
# Create your views here.


@login_required(login_url='login')
def chat_list(request):
    context = {}
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
    context = {}
    
    chat = Chat.objects.get(id=id)
    messages = Message.objects.filter(chat=chat)
    
    chat = generate_chat(chat, request.user)
    context['chat'] = chat
    context['messages'] = messages
    
    
    return render(request, 'chat.html', context)
