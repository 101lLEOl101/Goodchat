from __future__ import annotations

from .models import User
from .models import Profile

def get_profile(user:User) -> Profile:  
    profile = Profile.objects.get(user=user)
    return profile

def get_user(id:id) -> User | None:
    try:
        user = User.objects.get(id=id)
        return user
    except User.DoesNotExist:
        return None