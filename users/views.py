from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.contrib.auth.models import User
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')   
    def post(self, request):
        
        username =request.POST['username']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        password =request.POST['password']

        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
        )
        user.save()
        return redirect('user:login')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    