from .models import Bookmark
from users.models import User


def get_bookmarks(user: User):
    posts = list(Bookmark.objects.filter(user=user))
    print(posts)
    return posts