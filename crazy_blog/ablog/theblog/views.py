from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Comment
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import PostForm,EditPostForm,AddCommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        liked =False

        stuff = get_object_or_404(Post, id =  self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked =True
        
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes 
        context['liked'] = liked
        return context
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = ('title','author','body')
    #fields = '__all__'

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "update_post.html"

class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "confirm_delete.html"
    success_url= reverse_lazy('index')
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


class AddCategoryView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = "add_category.html"
    fields ='__all__'
    #--------------------------------------------------#

def CategoryView(request,cats):
    category_post = Post.objects.filter(cateogry__iexact = cats.replace('-' , ' '))
    return render(request,'category.html',{'cats':cats.title().replace('-' , ' ') , 'cat_post':category_post})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_list':cat_menu_list })

def LikeView(request,pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id') )
    liked =False

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked =False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "add_comment.html"
    #fields = ('title','author','body')
    #fields = '__all__'
    #success_url= reverse_lazy('index' )
    
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs['pk']})