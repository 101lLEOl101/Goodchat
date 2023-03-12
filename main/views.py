from django.shortcuts import render
from .forms import RegistrForm
from .forms import LogForm

def main_page(request):
 context = {}
 return render(request, "main_page.html", context)

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

 #Заглушка !!!!! !!! !! ! ! ! ! ! !  ! 
def login_page(request):
  data = {}
  form = LogForm()
  data['form'] = form
  return render(request, 'login.html', data)
 #Конец заглушки ( Давид К. )