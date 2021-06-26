from django import forms
from .models import Post,Category,Comment
#choices = [('coding','coding'),('space','space'),('food','food'),]

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title','title_tag','author','body','snippet','cateogry','header_image' )

        widgets = {
            'title': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'title_tag': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            #'author': forms.Select(attrs = {'class' :'form-control form-control-lg' }),
            'author': forms.TextInput(attrs = {'class' :'form-control form-control-lg','value':'','placeholder':'User name','id':'elder','type':'hidden'}),
            'body': forms.Textarea(attrs = {'class' :'form-control form-control-lg' }),
            'cateogry': forms.Select( choices=choice_list, attrs = {'class' :'form-control form-control-lg' }),
            'snippet' :forms.Textarea(attrs = {'class' :'form-control form-control-lg','placeholder':'Writhe your short story here limit to 250 Chars' }),
             
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title','cateogry','title_tag','body','snippet','header_image' )

        widgets = {
            'title': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'title_tag': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'body': forms.Textarea(attrs = {'class' :'form-control form-control-lg' }),
            'cateogry': forms.Select(choices=choices,attrs = {'class' :'form-control form-control-lg' }),
            'snippet' :forms.Textarea(attrs = {'class' :'form-control form-control-lg','placeholder':'Writhe your short story here limit to 250 Chars' })

        }



class AddCommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('name','body' )

        widgets = {
            'post': forms.Select(attrs = {'class' :'form-control form-control-lg'}),
            'name': forms.TextInput(attrs = {'class' :'form-control form-control-lg' }),
            'body': forms.Textarea(attrs = {'class' : 'form-control form-control-lg'}),
            
        }