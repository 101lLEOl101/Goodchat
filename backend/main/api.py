from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from users.models import User
from .serializers import PostSerializer
from .utils import get_bookmarks

class GetPost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        return Response({'post': PostSerializer.toDict(post, request.user)})
    
class GetUserPosts(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        author = get_object_or_404(User, id=id)
        posts = Post.objects.filter(author=author)
        posts = [PostSerializer.toDict(post, request.user)
                 for post in posts]
        
        return Response({'posts': reversed(posts)})
    
class GetFeed(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        posts = Post.objects.all()
        posts = [PostSerializer.toDict(post, request.user)
                 for post in posts]
        
        return Response({'posts': reversed(posts)})
    
class GetBookmarks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        posts = get_bookmarks(request.user)
        posts = [PostSerializer.toDict(post, request.user)
                 for post in posts]
        
        return Response({'posts': posts})
