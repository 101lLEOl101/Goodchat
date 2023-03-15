from django.shortcuts import render
from .forms import RegistrForm, LogForm


def main_page(request):
    context = {}
    return render(request, "main_page.html", context)

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
            data['res'] = "Всё прошло успешно"
            return render(request, 'reg.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
    return render(request, 'reg.html', data)


def settings_page(request):
    context = {}
    return render(request, "settings.html", context)


def settings_profile_page(request):
    context = {}
    return render(request, "settings_profile.html", context)

    # Заглушка !!!!! !!! !! ! ! ! ! ! !  !
