from django.contrib import admin

from .models import Contact, Head

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("fio", "email", "date", "login", "fio", "ipn", "name")

@admin.register(Head)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("firma", "adress", "phone", "site", "director", "fio")
