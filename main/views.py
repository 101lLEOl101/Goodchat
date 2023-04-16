from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import Profile
from users.models import User
from main.models import Post
from main.models import Comment
from .forms import PostForm
from .forms import CommentForm
from .forms import FrindSearchRequestForm
from itertools import groupby


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
                          } for post in reversed(posts)]
               }
    return render(request, 'main_page.html', context)


@login_required
def add_post_page(request):
    context = {}

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_author = request.user
            post_content = post_form.cleaned_data.get('content')
            post_photo = post_form.cleaned_data.get('photo')
            post = Post(author=post_author, content=post_content, photo=post_photo)
            post.save()
            return redirect('self-profile')

        context['form'] = post_form
        context['message'] = 'Incorrect form, try again'
    else:
        context['form'] = PostForm()

    return render(request, 'add_post_page.html', context)


@login_required
def find_friend_page(request):
    context = {}
    
    if request.method == 'POST':
        form = FrindSearchRequestForm(request.POST)
        if form.is_valid():
            response = []
            querry = form.data['querry']
            try:
                id = int(querry)
                response.extend(Profile.objects.filter(id=id))
            except ValueError:
                fullname = querry
                
                try:
                    name, surname = list(fullname.split())
                    response.extend(Profile.objects.filter(name=name, surname=surname))
                    response.extend(Profile.objects.filter(name=surname, surname=name))
                except ValueError:
                    name = fullname
                    surname = fullname
                
                response.extend([profile
                                 for profile 
                                 in Profile.objects.filter(name=name)
                                 if profile not in response])
                response.extend([profile 
                                 for profile 
                                 in Profile.objects.filter(surname=surname)
                                 if profile not in response])
                
            context['form'] = form                
            context['response'] = [profile for profile, _ in groupby(response)]
        else:
            context['form'] = form
            context['message'] = 'Incorrect request!'
    else:
        context['form'] = FrindSearchRequestForm()

    return render(request, 'find_friend_page.html', context)


@login_required
def bookmarks_page(request):
    return render(request, "bookmarks_page.html")

# Заглушка для проверки чужого профиля

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
                          'photo': post.photo,
                          'content': post.content,
                          'date': post.date_create,
                          } for post in reversed(posts)]
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
                             } for comment in reversed(comments)]
               }
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_author = request.user
            comment_content = comment_form.data['content']
            comment = Comment(author=comment_author, post=post, content=comment_content)
            comment.save()
        context['form'] = comment_form
        context['message'] = 'Incorrect form, try again'
    else:
        context['form'] = CommentForm()

    return render(request, 'post_template.html', context=context)
