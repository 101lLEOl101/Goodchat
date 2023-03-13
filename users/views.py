from django.shortcuts import render

from .models import Profile

# Create your views here.
def profile_page(request, id):
    print(Profile)
    return render(request, 'profile.html', context={'profile_id': id})
