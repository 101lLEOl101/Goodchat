from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import LoginForm
from .forms import RegistrationForm
from .forms import ProfileEditForm
from .models import User
from .models import Profile
from .signals import user_created


def registration_page(request):
    """
    View function which processes the user registration form 
    and performs the registration of new user.
    """
    if request.user.is_authenticated:
        return redirect('self-profile')

    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            context['form'] = form

            u_name = form.data['name']
            u_surname = form.data['surname']
            u_login = form.data['login']
            u_email = form.data['email']
            u_password = form.data['password']

            try:
                user = User.objects.create_user(username=u_login,
                                                email=u_email,
                                                password=u_password,
                                                is_active=True)

                user.save()

                user_created.send(sender=User,
                                  user=user,
                                  name=u_name,
                                  surname=u_surname)

                return redirect('login')
            except IntegrityError as error:
                context['form'] = form
                is_login_unique = False
                is_email_unique = False

                try:
                    User.objects.get(username=u_login)
                except User.DoesNotExist:
                    is_login_unique = True

                try:
                    User.objects.get(email=u_email)
                except User.DoesNotExist:
                    is_email_unique = True

                if not is_login_unique and not is_email_unique:
                    not_unique_fields = 'login, email'
                elif not is_login_unique:
                    not_unique_fields = 'login'
                elif not is_email_unique:
                    not_unique_fields = 'email'

                message = f"""
                User with this data is already registered, 
                check this fields: {not_unique_fields}.
                """

                context['message'] = message

                print(error)

        else:
            context['form'] = form
            
    else:
        context['form'] = RegistrationForm()

    return render(request, 'registration.html', context=context)


def login_page(request):
    """
    View function which processes the user authorization form 
    and performs the authorization.
    """
    if request.user.is_authenticated:
        return redirect('self-profile')
    
    context = {}

    if request.method == 'POST':
        auth_form = LoginForm(request.POST)

        if auth_form.is_valid():
            username = auth_form.data['username']
            password = auth_form.data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('self-profile')

            context['message'] = """
            Incorrect login or password - there is no user with such data
            """
            context['form'] = auth_form

        else:
            context['form'] = LoginForm()

    else:
        context['form'] = LoginForm()

    return render(request, 'login.html', context=context)


def profile_edit_page(request):
    context = {}

    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            context['form'] = form

            p_name = form.data['name']
            p_surname = form.data['surname']
            p_about = form.data['about']
            p_country = form.data['country']
            p_city = form.data['city']
            p_education = form.data['education']
            p_company = form.data['company']
            p_hobby = form.data['hobby']

            try:
                user = Profile.objects.filter(user=request.user).update(
                    name=p_name,
                    surname=p_surname,
                    about=p_about,
                    country=p_country,
                    city=p_city,
                    education=p_education,
                    company=p_company,
                    hobby=p_hobby
                )

                user.save()

                return redirect('profile_edit')
            except IntegrityError as error:
                return redirect('profile_edit')

        else:
            context['form'] = form

    else:
        context['form'] = ProfileEditForm()

    return render(request, 'registration.html', context=context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('home')
