from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forum_core.forms.settings import ProfileForm, PasswordlForm
from forum_core.widgets.forms import SectionForm
from forum_core.widgets.titles import PageTitle
from forum_core.services.upload import upload_file
from forum_core.models.settings import UserProfile


class SettingsView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request):
        user = request.user

        profile_form = ProfileForm(instance=user)
        password_form = PasswordlForm()
        user_profile = UserProfile.objects.get(user=user)

        if user_profile:
            profile_form.set_avatar(user_profile.avatar_url)
   
        return render(request, 'settings/index.html', { 
            "profile_form": profile_form, 
            "password_form": SectionForm().render("Password",password_form),
            "title":  PageTitle().render("Settings"),
        })
    
    @method_decorator(login_required(login_url="login"))
    def post(self, request):
        user = request.user

        if 'save_profile' in request.POST:
            form = ProfileForm(request.POST, instance=user)
            avatar_file = request.FILES.get('avatar')
                    
            if form.is_valid():
                form.save()
            
            if avatar_file: 
                is_uploaded, avatar_url = upload_file(avatar_file)
                if is_uploaded:
                    user_profile = UserProfile.objects.get(user=user)
                    if user_profile:
                        user_profile.avatar_url = avatar_url
                    else:
                        user_profile = UserProfile(user=user, avatar_url=avatar_url)
                    user_profile.save()

        if 'save_password' in request.POST:
            form = PasswordlForm(request.POST, instance=user)

            if form.is_valid() and form.check_password_confirmation():
                user.set_password(form['password'].value())
                user.save()


        return  self.get(request)


