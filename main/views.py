from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistrForm
from users.models import Profile


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
                           }
               }

    return render(request, 'profile.html', context=context)
