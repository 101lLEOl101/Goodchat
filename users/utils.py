from .models import User
from .models import Profile

def get_profile(user:User) -> Profile:  
    profile = Profile.objects.get(user=user)
    return profile