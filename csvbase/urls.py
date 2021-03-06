from django.urls import path
from django.views.generic import DetailView
from . models import Csvbase
from .views import print_act, print_dogovor, filter, read_file


urlpatterns = [

    path("print_act", print_act, name='print_act'),
    path("print_dogovor", print_dogovor, name='print_dogovor'),
    path('', filter, name='agrhouse'),
    path('pki-validation/44878CDDF2C235C196B8AAF73A2C3B34.txt', read_file),
    # path('', ListView.as_view(queryset=Csvbase.objects.all(), template_name="site/line_csvbase.html"), name="csv_link"),
    path('<pk>/', DetailView.as_view(model=Csvbase, template_name="site/doc1.html")),
]
