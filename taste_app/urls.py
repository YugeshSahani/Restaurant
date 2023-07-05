
from django.urls import path
from taste_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]