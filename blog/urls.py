from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('myposts/', views.my_posts, name='my_posts'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
