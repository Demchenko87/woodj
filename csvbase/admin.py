from django.contrib import admin

from .models import Csvbase, Agrhouse


@admin.register(Csvbase)
class CsvBase(admin.ModelAdmin):
    list_display = ("numb_lot", "p_lot", "seller", "product_name", "product_type", "product_kind", "product_diameter", "product_length", "storehouse", "product_size", "start_product_price", "start_lot_price", "EDRPOU")

@admin.register(Agrhouse)
class Agrhouse(admin.ModelAdmin):
    list_display = ("name", "director", "fio", "statut", "cod", "number_pdv", "individual_number", "adress", "mailing_address", "score", "phone", "email", "region")
