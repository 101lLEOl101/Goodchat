from __future__ import annotations

from .models import Message
from .models import Chat
from .models import Access
from django.db.models.fields.files import ImageFieldFile
from users.models import User
from main.models import Bookmark
from users.utils import get_profile


def get_chats(user) -> list:
    chats = [access.chat
             for access
             in Access.objects.filter(user=user)]
    
    return chats


def generate_chat(chat: Chat, current_user: User) -> dict:
    response = {'id': chat.id,
                'name': get_chat_name(chat, current_user),
                'avatar': get_chat_avatar(chat, current_user),
                'last_message': get_last_message(chat), }

    return response


def get_last_message(chat: Chat) -> Message:
    message = Message.objects.filter(chat=chat).last()
    return message


def get_chat_name(chat: Chat, current_user: User) -> str:
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


def get_chat_avatar(chat: Chat, current_user: User) -> ImageFieldFile:
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


def get_chat_messages(chat: Chat, current_user: User):
    messages_objects = Message.objects.filter(chat=chat)
    me = get_profile(current_user)

    messages = []
    for message_object in messages_objects:
        author = get_profile(message_object.author)

        if me == author:
            is_myown = True
        else:
            is_myown = False

        message = {
            'author': author.name,
            'content': message_object.content,
            'date_create': message_object.date_create,
            'is_myown': is_myown,
        }

        messages.append(message)

    return messages


def send_message(chat, author, content):
    message = Message(chat=chat,
                      author=author,
                      content=content,
                      is_read=False)
    message.save()


def create_dialog(user1: User, user2: User) -> Chat:
    dialog = Chat(is_multy=False)
    dialog.save()
    access1 = Access(chat=dialog, user=user1, mode=4)
    access2 = Access(chat=dialog, user=user2, mode=4)
    access1.save()
    access2.save()
    return dialog


def dialog_created(user1: User, user2: User) -> Chat | None:
    user1_chats = get_chats(user1)
    for chat in user1_chats:
        if not chat.is_multy:
            try:
                user2_access = Access.objects.get(user=user2, chat=chat)
                return chat
            except Access.DoesNotExist:
                continue
            
    return None


def get_dialog(user1, user2) -> None:
    dialog = dialog_created(user1, user2)
    if dialog is not None:
        return dialog
    else:
        return create_dialog(user1, user2)

        
