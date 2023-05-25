from typing import Optional

from .models import User
from .models import Profile
from .models import Friend
from .models import FriendRequest
from .models import FriendRequest


def get_profile(user: User) -> Profile:
    profile = Profile.objects.get(user=user)
    return profile


def convert_profile_to_dict(profile: Profile):
    profile_dict = {'id': profile.id,
                    'name': profile.name,
                    'surname': profile.surname,
                    'full_name': f'{profile.name} {profile.surname}',
                    'avatar': profile.avatar}
    return profile_dict


def get_user(id:id) -> Optional[User]:
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


def are_friends(user1: User, user2: User) -> bool:
    user1_friends = get_friends(user1)
    return user2 in user1_friends


def friend_able_to_invite(inviter, recipient) -> bool:
    if inviter == recipient:
        return False

    if are_friends(inviter, recipient):
        return False

    try:
        invitation = FriendRequest.objects.get(
            inviter=inviter, recipient=recipient)
    except FriendRequest.DoesNotExist:
        pass
    else:
        return False

    try:
        invitation = FriendRequest.objects.get(
            inviter=recipient, recipient=inviter)
    except FriendRequest.DoesNotExist:
        pass
    else:
        return False

    return True

def friend_invited(inviter: User, recipient: User) -> bool:
    try: 
        invitation = FriendRequest.objects.get(inviter=inviter, recipient=recipient)
    except FriendRequest.DoesNotExist:
        return False
    else:
        return True

def accept_friend_request(inviter: User, recipient: User):
    try:
        invitation = FriendRequest.objects.get(inviter=inviter, recipient=recipient)
    except FriendRequest.DoesNotExist:
        raise ValueError('Null request can\'t be accepted')
    else:
        friendship = Friend()
        friendship.save()
        friendship.friends.set([inviter, recipient])
        friendship.save()
        invitation.delete()
        
def get_friend_add_button_state(user_id: User, opponent_id: User):
    user = User.objects.get(id=user_id)
    opponent = User.objects.get(id=opponent_id)
    state = False
    if friend_invited(opponent, user):
        state = 'Accept friendship'
    elif friend_invited(user, opponent):
        state = 'Cancel friend request'
    elif friend_able_to_invite(user, opponent):
        state = 'Offer friendship'
    elif are_friends(user, opponent):
        state = 'Stop being friends'
    
    return state 

def refuse_friendship(user1: User, user2: User):
    user1_friendships = Friend.objects.filter(friends__in=[user1])
    for friendship in user1_friendships:
        if user2 in friendship.friends.all():
            friendship.delete()
            return
        
    print('error: no friendships')

def deny_friend_request(inviter: User, recipient: User):
    invitation = FriendRequest.objects.get(inviter=inviter, recipient=recipient)
    invitation.delete()
