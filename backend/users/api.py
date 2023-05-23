from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .serializers import FriendSerializer
from .models import User
from .signals import user_created
from .utils import get_friends
from .utils import refuse_friendship


class Register(APIView):
    def post(self, request, format=None):
        user_data = dict(request.data)
        response = {}
        
        try:
            user = User.objects.create_user(username=user_data['login'],
                                            email=user_data['email'],
                                            password=user_data['password'],
                                            is_active=True)
            
            user.save()

            user_created.send(sender=User,
                            user=user,
                            name=user_data['name'],
                            surname=user_data['surname'])
            
            response['status'] = 'success'
            response['message'] = 'User registered successfully'
            response['user'] = UserSerializer.toFullProfileDict(user)
             
        except IntegrityError as error:
            response['status'] = 'error'
            response['message'] = 'User with the same data is already exists'
        
        return Response(response)
    

class SelfProfile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        user = UserSerializer.toFullProfileDict(request.user)
        response = {'user': user}
        return Response(response)
    
class GetProfile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id, format=None):
        user = get_object_or_404(User, id=id)
        response = {'user': UserSerializer.toFullProfileDict(user)}
        return Response(response)
    
class GetFriendList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        user_friends = get_friends(user)
        user_friends = [FriendSerializer.toDict(friend)
                        for friend in user_friends]
        
        return Response({'friends': user_friends})
    
class RefuseFriendship(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def refuse_request_permission(self, user_id, user1_id, user2_id):
        return user_id == user1_id or user_id == user2_id
    
    def post(self, request):
        user1 = get_object_or_404(User, id=request.data['user1_id'])
        user2 = get_object_or_404(User, id=request.data['user2_id'])
        if not self.refuse_request_permission(request.user.id,
                                              user1.id, 
                                              user2.id):
            raise PermissionError('It\'s not your friendship!!!')
        
        refuse_friendship(user1, user2)