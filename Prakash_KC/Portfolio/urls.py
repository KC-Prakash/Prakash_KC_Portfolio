from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about-me/', views.about_me, name='about_me'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills', views.skills, name='skills'),


]