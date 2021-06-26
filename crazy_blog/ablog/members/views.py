from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import   UserCreationForm, UserChangeForm
from django.contrib.auth.views import   PasswordChangeView
from .forms import SiginUpForm,EditSettingsForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import PasswordChangingForm ,EditProfileForm,CreateProfileForm
from django.views.generic import ListView ,DetailView
from theblog.models import Profile
# Create your views here.


class CreateProfileView(generic.CreateView):
    model = Profile
    template_name = "registration/create_profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProfileView, self).form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    #fields = ['bio','profile_pic','website_url','facebook_url','instagram_url','other_url']
    form_class =EditProfileForm
    success_url = reverse_lazy('index')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context



class UserRegisterView(generic.CreateView):
    form_class= SiginUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class= EditSettingsForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class =PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html',{})