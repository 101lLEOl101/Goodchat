from django.shortcuts import render

from models import Profile

# Create your views here.
def profile_page(request):
    return render(request, 'profile_page.html', context={
        'user': Profile.user,
        'name': Profile.name,
        'surname': Profile.surname,
        'avatar': Profile.avatar,
        'about': Profile.about,
        'country': Profile.country,
        'city': Profile.city,
        'education': Profile.education,
        'company': Profile.company,
        'hobby': Profile.hobby,
    })
