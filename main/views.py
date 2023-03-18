from django.shortcuts import render
from django.shortcuts import redirect
from users.models import Profile
from users.models import User
from main.models import Post
from main.models import Comment
from .forms import RegistrForm


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)

def bookmarks_page(request):
    context = {}
    return render(request, "bookmarks_page.html", context)


def regist(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = 'Всё прошло успешно'
            return render(request, 'reg.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
    return render(request, 'reg.html', data)


def settings_page(request):
    context = {}
    return render(request, 'settings.html', context)


def settings_profile_page(request):
    context = {}
    return render(request, 'settings_profile.html', context)

    # Заглушка !!!!! !!! !! ! ! ! ! ! !  !


def profile(request, id:int):
    """
    View function which represents page with wall of the current user by id
    """
    try:
        profile = Profile.objects.get(id=id)
        user = User.objects.get(id=id)
        posts = Post.objects.filter(author=user)
    except Profile.DoesNotExist:
        return redirect('home')

    context = {'profile': {'id': profile.id,
                           'name': profile.name,
                           'surname': profile.surname,
                           'avatar': profile.avatar,
                           'about': profile.about,
                           'country': profile.country,
                           'city': profile.city,
                           'education': profile.education,
                           'company': profile.company,
                           'hobby': profile.hobby,
                           },
               'posts': [{'id': post.id,
                          'author': post.author,
                          'content': post.content,
                          'date': post.date,
                          } for post in posts]
               }

    return render(request, 'profile.html',  context=context)


def post(request, id:int):
    """
    View function which represents the page with current post by id 
    and comments for that post
    """
    try:
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post)
    except Post.DoesNotExist:
        return redirect('home')

    context = {'post': {'id': post.id,
                        'author': post.author,
                        'content': post.content,
                        'date': post.date,
                        },
               'comments': [{'author': comment.author,
                             'content': comment.content,
                             'date': comment.date
                             } for comment in comments]
               }

    return render(request, 'post_template.html', context=context)