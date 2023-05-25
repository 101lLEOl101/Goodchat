from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Chat
from .models import Message
from users.models import User
from .utils import chat_access
from .utils import get_chats
from .utils import get_dialog
from .serializers import ChatSerializer

class GetChat(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        access = chat_access(request.user.id, id)
        if access and access.mode != 0:
            chat = access.chat
        else:
            raise PermissionDenied
        
        chat = ChatSerializer.chatToFullDict(chat, request.user)
        return Response({'chat': chat})
    
class GetChatlist(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        chats = get_chats(request.user)
        print(*chats)
        normilized_chats = []
        for chat in chats:
            normilized_chat = ChatSerializer.chatToItemDict(chat, request.user)
            if normilized_chat:
                normilized_chats.append(normilized_chat)
        
        return Response({'chats': normilized_chats})
    
class SendMessage(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        chat_id = request.data['chat_id']
        user = request.user
        content = request.data['content']
        chat = get_object_or_404(Chat, id=chat_id)
        access = chat_access(user.id, chat_id)
        
        if not access or access.mode == 0:
            raise PermissionDenied
        
        message = Message(chat=chat, author=user, content=content)
        message.save()
        print(message);
        message = ChatSerializer.messageToDict(message, user)
        return Response({'message': message})
        
class GetDialog(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        interlocutor = get_object_or_404(User, id=id)
        dialog = get_dialog(request.user, interlocutor)
        
        return Response({'dialog_id': dialog.id})