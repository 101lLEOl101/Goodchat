from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from users.models import User
from main.models import Post
from main.models import Comment
from .forms import PostForm


@login_required
def self_profile(request):
    return redirect(f'/profile/{request.user.id}')


def main_page(request):
    posts = Post.objects.all()
    context = {'posts': [{'id': post.id,
                          'author': post.author,
                          'photo': post.photo,
                          'content': post.content,
                          'date': post.date_create,
                          } for post in posts]
               }
    return render(request, 'main_page.html', context)


@login_required
def add_post_page(request):
    context = {}

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_author = request.user
            post_content = post_form.data['content']
            post = Post(author=post_author, content=post_content)
            post.save()
            return redirect('self-profile')

        context['form'] = post_form()
        context['message'] = 'Incorrect form, try again'
    else:
        context['form'] = PostForm()

    return render(request, 'add_post_page.html', context)


@login_required
def find_friend_page(request):
    return render(request, 'find_friend_page.html')


@login_required
def bookmarks_page(request):
    return render(request, "bookmarks_page.html")

# Заглушка для проверки чужого профиля


def diff_profile_page(request, id: int):
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
                          'date': post.date_create,
                          } for post in posts]
               }

    return render(request, 'profile_diffrent.html', context=context)


@login_required
def settings_page(request):
    return render(request, 'settings.html')


@login_required
def chat_page(request):
    return render(request, 'chat_list.html')


@login_required
def messenger_page(request):
    return render(request, 'messenger.html')


@login_required
def settings_profile_page(request, id: int):
    profile = Profile.objects.get(id=id)

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
                           }
               }

    return render(request, 'settings_profile.html', context=context)

    # Заглушка !!!!! !!! !! ! ! ! ! ! !  !


def profile(request, id: int):
    """
    View function which represents page with wall of the current user by id
    """
    try:
        user = User.objects.get(id=id)
    except:
        return redirect('home')
    
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user)

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
                          'author': {'name': post.author,
                                     'link': f'/profile/{post.author.id}',
                                     },
                          'content': post.content,
                          'date': post.date_create,
                          } for post in posts]
               }

    return render(request, 'profile.html',  context=context)


def post(request, id: int):
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
                        'author': {'name': post.author,
                                   'link': f'/profile/{post.author.id}',
                                   },
                        'content': post.content,
                        'photo': post.photo,
                        'date': post.date_create,
                        },
               'comments': [{'author': comment.author,
                             'content': comment.content,
                             'date': comment.date_create
                             } for comment in comments]
               }

    return render(request, 'post_template.html', context=context)
