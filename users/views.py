from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, get_user_model, authenticate
# Create your views here.
User = get_user_model()


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        username = data['uname']
        password = data['psw']
        user = authenticate(
            username=username, password=password)
        login(request, user)
        return redirect('/')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = request.POST

        username = data['uname']
        password = data['psw']
        email = data['email']
        user = User.objects.create_user(
            username=username, password=password, email=email)
        user.save()
        return redirect('/users/login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
