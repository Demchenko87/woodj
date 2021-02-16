from django.shortcuts import render
from django.views.generic.base import View
from .models import Slider, AboutUs, Services, Partners, Auctions

class MainPage(View):
    def get(self, request):
        slider = Slider.objects.all()
        about = AboutUs.objects.all()
        services = Services.objects.all()
        partners = Partners.objects.all()

        return render(request, "site/index.html", {"slider_list": slider,
                                                   "about_list": about,
                                                   "services_list": services,
                                                   "partners_list": partners,
                                                   })

class ServicesPage(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, "site/services.html", {"services_list": services})

class AuctionsPage(View):
    def get(self, request):
        auctions = Auctions.objects.all()
        return render(request, "site/auctions.html", {"auctions_list": auctions})

class ContactsPage(View):
    def get(self, request):
        return render(request, "site/contact.html")

class ThanksPage(View):
    def get(self, request):
        return render(request, "site/thanks.html")

class PodachaPage(View):
    def get(self, request):
        return render(request, "site/podacha.html")

class LoginPage(View):
    def get(self, request):
        return render(request, "site/login.html")
