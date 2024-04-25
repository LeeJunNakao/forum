from django.views import View
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.shortcuts import render, redirect
from forum_core.forms.auth import LoginForm

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html', { "login_form": LoginForm()})
    
    def post(self, request):
        form = LoginForm(request.POST)

        user = authenticate(username=form['username'].value(), password=form['password'].value())
        if user is not None:
            do_login(request, user)
            return redirect('homepage')

class LogoutView(View):
    def get(self, request):
        do_logout(request)
        return redirect('homepage')