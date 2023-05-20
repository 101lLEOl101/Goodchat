from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .models import User
from .signals import user_created


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