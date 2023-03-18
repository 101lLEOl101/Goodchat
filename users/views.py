from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .forms import LoginForm
from .forms import RegistrationForm
from .models import User
from .signals import user_created
from .signals import create_profile


def registration_page(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            context['form'] = form

            name = form.data['name']
            surname = form.data['surname']
            login = form.data['login']
            email = form.data['email']
            password = form.data['password']

            try:
                user = User.objects.create_user(username=login,
                                                email=email,
                                                password=password,
                                                is_active=True)
                
                user.save()
                
                # user_created.connect(create_profile, 
                #                      dispatch_uid=user.id)
                
                user_created.send(sender=User, 
                                  user=user,
                                  name=name, 
                                  surname=surname)
                
                request.user = user
                
                return redirect(f'/profile/{request.user.id}')
            except IntegrityError as error:
                context['form'] = form
                print(error)
                

        else:
            context['form'] = form

    return render(request, 'registration.html', context=context)


def login_page(request):
    """
    View function which processes the user authorization form 
    and performs the authorization.
    """
    context = {}

    if request.method == 'POST':
        auth_form = LoginForm(request.POST)

        if auth_form.is_valid():
            username = auth_form.data['username']
            password = auth_form.data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                current_user_id = request.user.id
                return redirect(f'/profile/{current_user_id}')
            else:
                context['message'] = 'Error: bad login/password'
                context['form'] = auth_form

        else:
            context['message'] = 'Error: invalid form'
            context['form'] = LoginForm()

    else:
        context['message'] = 'Waiting for user data'
        context['form'] = LoginForm()

    return render(request, 'login.html', context=context)
