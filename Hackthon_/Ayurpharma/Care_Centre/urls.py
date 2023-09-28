from django.contrib import admin
from django.urls import path, include
from Care_Centre import views

urlpatterns = [
    path('',views.index, name="home"),
    path('about_us',views.about, name="about_us"),
    path('Ayurvedic_treatment',views.search, name="Ayurvedic_tretment"),
    path('result',views.result, name="result"),
    path('blog',views.blog, name="blog"),
    path('contact_us',views.contact, name="contact"),
    path('thank_you',views.thanks, name="thanks"),
    
    
]