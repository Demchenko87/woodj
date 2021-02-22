from django.contrib import admin

from .models import Contact, Head

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "date", "login", "fio")

@admin.register(Head)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("firma", "adress", "phone", "site", "director", "fio")
