from .models import Bookmark
from users.models import User
from .models import Post

def get_bookmarks(user: User):
    posts = [bookmark.post 
             for bookmark in Bookmark.objects.filter(user=user)]
    return posts

def is_in_bookmark(user: User, post: Post):
    return 1 if Bookmark.objects.filter(user=user, post=post) else 0