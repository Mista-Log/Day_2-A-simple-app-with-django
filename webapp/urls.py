from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('team', views.team, name='team'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('blog-details', views.blog_details, name='blog_details'),
    path('portfolio-details', views.portfolio_details, name='portfolio_details'),
]

