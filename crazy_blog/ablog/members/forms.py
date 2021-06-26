from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from theblog.models import Profile

class SiginUpForm(UserCreationForm):
   
    email = forms.EmailField(  required=False ,  widget = forms.EmailInput(attrs =   {'class' :'form-control ' }  )  )
    first_name = forms.CharField( max_length=200, required=True,widget=forms.TextInput(attrs = {'class' :'form-control ' }))
    last_name = forms.CharField( max_length= 200, required=False,widget =forms.TextInput(attrs = {'class' :'form-control ' }))
    class Meta:
            model = User
            fields = ('username','first_name','last_name','email','password1','password2')
            
    
    def __init__(self, *args, **kwargs):
        super(SiginUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'




class EditSettingsForm(UserChangeForm):
   
    email = forms.EmailField(  required=False ,  widget = forms.EmailInput(attrs =   {'class' :'form-control ' }  )  )
    first_name = forms.CharField( max_length=200, required=True,widget=forms.TextInput(attrs = {'class' :'form-control ' }))
    last_name = forms.CharField( max_length= 200, required=False,widget =forms.TextInput(attrs = {'class' :'form-control ' }))
    username = forms.CharField( max_length= 200, required=False,widget =forms.TextInput(attrs = {'class' :'form-control ' }))
    last_login = forms.CharField( max_length= 200, required=False,widget =forms.TextInput(attrs = {'class' :'form-control ' }))
    is_superuser = forms.CharField( max_length= 200, required=False,widget =forms.CheckboxInput(attrs = {'class' :'form-check ' }))
    is_staff = forms.CharField( max_length= 200, required=False,widget =forms.CheckboxInput(attrs = {'class' :'form-check ' }))
    is_active = forms.CharField( max_length= 200, required=False,widget =forms.CheckboxInput(attrs = {'class' :'form-check ' }))
    date_joined = forms.CharField( max_length= 200, required=False,widget =forms.TextInput(attrs = {'class' :'form-control ' }))
    
    
    class Meta:
            model = User
            fields = ('username','first_name','last_name','email','password','last_login','is_superuser','is_staff','is_active','date_joined')
            


class PasswordChangingForm(PasswordChangeForm):
   
    old_password = forms.EmailField(  required=False ,  widget = forms.PasswordInput(attrs =   {'class' :'form-control ','type':'password' }  )  )
    new_password1 = forms.CharField( max_length=200, required=True,widget=forms.PasswordInput(attrs = {'class' :'form-control ' ,'type':'password'}))
    new_password2 = forms.CharField( max_length= 200, required=False,widget =forms.PasswordInput(attrs = {'class' :'form-control ' ,'type':'password'}))
    class Meta:
            model = User
            fields = ('old_password','new_password1','new_password2')
   
class EditProfileForm(forms.ModelForm):
        """Form definition for MODELNAME."""

        class Meta:
                """Meta definition for MODELNAMEform."""

                model = Profile
                fields = ('bio','profile_pic','website_url','facebook_url','instagram_url','other_url')
                widgets = {
            'bio': forms.Textarea(attrs = {'class' :'form-control form-control-lg' }),
            'website_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'facebook_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'instagram_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'other_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
        }

class CreateProfileForm(forms.ModelForm):
        """Form definition for MODELNAME."""

        class Meta:
                """Meta definition for MODELNAMEform."""

                model = Profile
                fields = ('bio','profile_pic','website_url','facebook_url','instagram_url','other_url')
                widgets = {
            'bio': forms.Textarea(attrs = {'class' :'form-control form-control-lg' }),
            'website_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'facebook_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'instagram_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'other_url': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
        }