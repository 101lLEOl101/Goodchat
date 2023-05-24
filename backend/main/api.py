from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .models import Comment
from users.models import User
from .serializers import PostSerializer
from .serializers import CommentSerializer
from .utils import get_bookmarks
from .utils import get_comments

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
    
class GetComments(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = get_comments(post)
        comments = [CommentSerializer.toDict(comment)
                    for comment in comments]
        
        return Response({'comments': comments})

class SendComment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        author = request.user
        content = request.data['content']
        post_id = request.data['post_id']
        post = get_object_or_404(Post, id=post_id)
        comment = Comment(post=post, author=author, content=content)
        comment.save()
        
        return Response({'comment': CommentSerializer.toDict(comment)})
    
class AddPost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        content = request.data['content']    
        photo = request.data['photo']
        print(content, photo)
        post = Post(author=request.user, 
                    content=content, 
                    photo=photo)
        post.save()
        
        return Response({'id': post.id})