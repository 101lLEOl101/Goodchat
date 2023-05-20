from .models import User 
from .models import Profile 
from .utils import get_profile

def imageToUrl(image):
        if image:
            return f'http://127.0.0.1:8000{image.url}'  
        return image
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
            'avatar': imageToUrl(profile.avatar),
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
            'avatar': imageToUrl(profile.avatar),
            'about': profile.about,
            'country': profile.country,
            'city': profile.city,
            'education': profile.education,
            'company': profile.company,
            'hobby': profile.hobby,
        }
        
        return response