from django.urls import path
from django.views.generic import ListView, DetailView
from . models import Csvbase
from .views import print_act, print_dogovor


urlpatterns = [

    path("print_act", print_act, name='print_act'),
    path("print_dogovor", print_dogovor, name='print_dogovor'),
    path('', ListView.as_view(queryset=Csvbase.objects.all(), template_name="site/line_csvbase.html"), name="csv_link"),
    path('<pk>/', DetailView.as_view(model=Csvbase, template_name="site/doc1.html")),
]
