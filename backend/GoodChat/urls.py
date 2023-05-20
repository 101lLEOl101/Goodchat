"""GoodChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views
from main import api as main_api
from users import views as users_views
from users import api as users_api
from chat import views as chat_views
from chat import api as chat_api 
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/register', users_api.Register.as_view()),
    path('api/profile/self', users_api.SelfProfile.as_view()),
    path('api/profile/<int:id>', users_api.GetProfile.as_view()),
    
    path('api/post/<int:id>', main_api.GetPost.as_view()),
    path('api/post/getUserPosts/<int:id>', main_api.GetUserPosts.as_view()),
    path('api/post/getFeed', main_api.GetFeed.as_view()),
    path('api/bookmarks', main_api.GetBookmarks.as_view()),
    
    path('api/chat/<int:id>', chat_api.GetChat.as_view()),
    path('api/chatlist', chat_api.GetChatlist.as_view()),
    
    path('admin/', admin.site.urls),
    path('', main_views.main_page, name='home'),
    path('bookmarks', main_views.bookmarks_page, name='bookmarks'),
    path('add-bookmark/<int:post_id>', main_views.add_or_delete_bookmark, name='add-delete-bookmark'),
    path('settings/', main_views.settings_page, name='setting'),
    path('edit/', users_views.settings_profile, name = 'edit'),
    path('login/', users_views.login_page, name='login'),
    path('register/', users_views.registration_page, name='registration'),
    path('logout/', users_views.logout_page, name='logout'),
    path('profile/<int:id>', main_views.profile, name = 'profile'),
    path('profile', main_views.self_profile, name='self-profile'),
    path('post/<int:id>', main_views.post, name='post'),
    path('postedit/<int:id>', main_views.edit_post, name='postedit'),
    path('addpost', main_views.add_post_page, name = 'addpost'),
    path('findfriend', main_views.find_friend_page, name = 'findfriend'),
    path('messenger', main_views.messenger_page, name='messenger'),
    path('chatlist', chat_views.chat_list, name='chat-list'),
    path('chat/<int:id>', chat_views.chat_page, name='chat'),
    path('dialog/<int:interlocutor_id>', chat_views.open_dialog, name='open-dialog'),
    path('friendlist/<int:id>', users_views.friend_list, name='friend-list'),
    path('addfriend/<int:recipient_id>', users_views.invite_friend, name='add-friend'),
    path('reject_request/<int:recipient_id>', users_views.reject_request_friend, name='reject_request_friend'),
    path('chat/info/<int:chat_id>', chat_views.multichat_info, name='multychat-info'),   
    path('chat/settings/<int:chat_id>', chat_views.multichat_settings, name='multychat-settings'),   
    path('chat/leave/<int:chat_id>', chat_views.leave_chat, name='leave-chat'),   
    path('chat/new/multy', chat_views.new_multychat, name='new-multychat'),
    path('postdelete/<int:id>', main_views.post_delete, name = 'postdelete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)