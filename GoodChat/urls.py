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
from users import views as users_views
from chat import views as chat_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main_page, name='home'),
    path('bookmarks', main_views.bookmarks_page, name='bookmarks'),
    path('settings/', main_views.settings_page, name='setting'),
    path('settingsprofile/<int:id>', main_views.settings_profile_page),
    path('login/', users_views.login_page, name='login'),
    path('register/', users_views.registration_page, name='registration'),
    path('logout/', users_views.logout_page, name='logout'),
    path('profile/<int:id>', main_views.profile),
    path('profile/', main_views.self_profile, name='self-profile'),
    path('post/<int:id>', main_views.post),
    path('addpost', main_views.add_post_page, name = 'addpost'),
    path('findfriend', main_views.find_friend_page, name = 'findfriend'),
    path('chat', main_views.chat_page, name = 'chat'),
    path('messenger', main_views.messenger_page, name='messenger'),
    #плохие ссылки
    path('settingsprofile/1', main_views.settings_profile_page, name = 'settingsprofile/1'),
    path('profile/1',main_views.find_friend_page, name = 'profile/1'),
    
    path('chatlist', chat_views.chat_list, name='chat-list'),
    path('chat/<int:id>', chat_views.chat_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)