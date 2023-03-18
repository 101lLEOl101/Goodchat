from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistrForm
from users.models import Profile
from main.models import Post
from main.models import Comment


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


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


def profile(request, id):
    """
    View function which represents page with wall of the current user
    """
    try:
        profile = Profile.objects.get(id=id)
        post = Post.objects.all()
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
               'posts': {'id': post.id,
                           'author': post.author,
                           'content': post.content,
                           'date': post.date,
               }
               }

    return render(request, 'profile.html', 'post_template',  context=context)


def post(request, id):
    try:
        post = Post.objects.get(id=id)
        comment = Comment.objects.filter(post=post)
    except Post.DoesNotExist:
        return redirect('home')

    context = {'post': {'id': post.id,
                           'author': post.author,
                           'content': post.content,
                           'date': post.date,
                           },
               'comment': {
                           'author': comment.author,
                           'content': comment.content,
                           'date': comment.date,
               }
               }

    return render(request, 'post_template', context=context)
