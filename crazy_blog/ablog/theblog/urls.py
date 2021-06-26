
from django.contrib import admin
from django.urls import path,include
from .import views
from .views import AddCommentView, AddCategoryView,HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView
urlpatterns = [
    path('', HomeView.as_view() ,name='index'),
    path('article/<str:pk>/', ArticleDetailView.as_view() ,name='article_detail'),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path('article/edit/<str:pk>/',UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<str:pk>/',DeletePostView.as_view(),name ='delete_post'),
    
    path('add_category/',AddCategoryView.as_view(),name= 'add_category'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category_list/',views.CategoryListView,name ='category_list'),
    #--------------------------------------------------------------------------------------#
    path('like_post/<str:pk>',views.LikeView,name='like_post'),
    path('article/<str:pk>/add_comment/',AddCommentView.as_view(),name='add_comment')
]
