from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (DropdownFilter)
from .models import Csvbase, Agrhouse


@admin.register(Csvbase)
class CsvBase(admin.ModelAdmin):
    list_display = ("date", "numb_lot", "p_lot", "seller", "buyer", "product_name", "product_type", "product_kind", "product_diameter", "product_length", "storehouse", "product_size", "start_product_price", "start_lot_price", "EDRPOU")
    list_filter = (
	    ('date', DropdownFilter),
	    ('seller', DropdownFilter),
	    ('buyer', DropdownFilter),
	    ('EDRPOU', DropdownFilter),
    )

@admin.register(Agrhouse)
class Agrhouse(admin.ModelAdmin):
    list_display = ("name", "director", "fio", "statut", "cod", "number_pdv", "individual_number", "adress", "mailing_address", "score", "phone", "email", "region")
