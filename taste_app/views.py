from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'taste/main/index.html'

class AboutView(TemplateView):
    template_name = 'taste/about.html'

class ServiceView(TemplateView):
    template_name = 'taste/service.html'

class MenuView(TemplateView):
    template_name = 'taste/menu.html'

class ContactView(TemplateView):
    template_name = 'taste/contact.html'

class BookingView(TemplateView):
    template_name = 'taste/booking.html'