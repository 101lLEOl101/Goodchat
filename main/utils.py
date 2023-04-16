from .models import Bookmark
from users.models import User


def get_bookmarks(user: User):
    posts = [bookmark.post 
             for bookmark in Bookmark.objects.filter(user=user)]
    print(posts)
    
    return posts