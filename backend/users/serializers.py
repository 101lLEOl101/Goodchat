from .models import User 
from .models import Profile 
from .utils import get_profile


class UserSerializer:
    def toUserDict(user:User) -> dict:
        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        
        return response
    
    def toShortProfileDict(user: User) -> dict:
        profile = get_profile(user)
        response = {
            'id': user.id,
            'name': profile.name,
            'surname': profile.surname,
            'login': user.username,
            'email': user.email,
            'avatar': profile.avatar.url
        }
        
        return response
        
    def toFullProfileDict(user: User) -> dict:
        profile = get_profile(user)
        response = {
            'id': user.id,
            'name': profile.name,
            'surname': profile.surname,
            'login': user.username,
            'email': user.email,
            'avatar': profile.avatar.url,
            'about': profile.about,
            'country': profile.country,
            'city': profile.city,
            'education': profile.education,
            'company': profile.company,
            'hobby': profile.hobby,
        }
        
        return response