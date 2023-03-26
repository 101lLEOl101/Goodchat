from .models import Message
from .models import Chat
from .models import Access
from django.db.models.fields.files import ImageFieldFile
from users.models import User
from users.utils import get_profile

def generate_chat(chat:Chat, current_user:User) -> dict:
    response = {'id': chat.id,
                'name': get_chat_name(chat, current_user),
                'avatar': get_chat_avatar(chat, current_user),
                'last_message': get_last_message(chat),}
    return response

def get_last_message(chat:Chat) -> Message:
    message = Message.objects.filter(chat=chat).last()
    return message

def get_chat_name(chat:Chat, current_user:User) -> str:
    if chat.is_multy:
        return chat.name
    
    members = [access.user 
                for access
                in Access.objects.filter(chat=chat)]
    
    for member in members:
        if member == current_user:
            continue
        friend = member

    friend = get_profile(friend)
        
    return f'{friend.name} {friend.surname}'

def get_chat_avatar(chat:Chat, current_user:User) -> ImageFieldFile:
    if chat.is_multy:
        return chat.avatar
    
    members = [access.user 
                for access
                in Access.objects.filter(chat=chat)]
    
    for member in members:
        if member == current_user:
            continue
        friend = member

    friend = get_profile(friend)
        
    return friend.avatar