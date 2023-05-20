from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Chat
from .utils import chat_access
from .utils import get_chats
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
        chats = [ChatSerializer.chatToItemDict(chat, request.user)
                 for chat in chats]
        
        return Response({'chats': chats})
        