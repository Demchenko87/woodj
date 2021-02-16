from django.urls import path, include
from . import views




urlpatterns = [
    path("", views.MainPage.as_view(), name='index'),
    path('services/', views.ServicesPage.as_view(), name='services'),
    path('auctions/', views.AuctionsPage.as_view(), name='auctions'),
    path('contacts/', views.ContactsPage.as_view(), name='contacts'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),

    path('csvbase/', include('csvbase.urls')),

    path('podacha/', views.PodachaPage.as_view(), name='podacha'),
    path('login/', views.LoginPage.as_view(), name='login'),
]
