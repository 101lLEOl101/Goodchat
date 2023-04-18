from .models import User
from .models import Profile
from .models import Friend

def get_profile(user:User) -> Profile:  
    profile = Profile.objects.get(user=user)
    return profile

def get_user(id:id) -> User | None:
    try:
        user = User.objects.get(id=id)
        return user
    except User.DoesNotExist:
        return None
    
def get_friends(user: User):
    def get_friend(friendship: Friend):
        friends = list(friendship.friends.all())
        
        if len(friends) > 2:
            raise ValueError(f'Friends is a pair of users, not {len(friends)}')   
             
        for friend in friends:
            if friend != user:
                return friend
        raise ValueError('User cannot be friends with himself')
    
    friends = [get_friend(friendship)
               for friendship in user.friend_with.all()]
    
    return friends