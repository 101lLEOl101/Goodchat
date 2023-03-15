from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import LoginForm


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



