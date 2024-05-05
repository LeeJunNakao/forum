from django.views import View
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.shortcuts import render, redirect
from forum_core.models.topic import User
from forum_core.forms.auth import LoginForm, RegisterForm
from forum_core.widgets.titles import PageTitle

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html', { "login_form": LoginForm()})
    
    def post(self, request):
        form = LoginForm(request.POST)

        user = authenticate(username=form['username'].value(), password=form['password'].value())
        if user is not None:
            do_login(request, user)
            return redirect('homepage')
        
        return self.get(request)

class LogoutView(View):
    def get(self, request):
        do_logout(request)
        return redirect('homepage')

class RegisterView(View):
    def get(self, request):
    
        return render(request, 'auth/register.html', { "title":  PageTitle().render("Register"), "form": RegisterForm() })
    
    def post(self, request):
        form = RegisterForm(request.POST)

        print("??????????????????????????????", form.is_valid())
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.set_password(form.cleaned_data['password'])
            user.save()


        return redirect('homepage')
        # return redirect('login')