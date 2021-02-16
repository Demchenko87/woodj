from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Slider, AboutUs, Services, Partners, Auctions


class WebsiteAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AboutUs
        fields = '__all__'

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("content",)
    list_display_links = ("content",)
    form = WebsiteAdminForm

@admin.register(Auctions)
class AuctionsAdmin(admin.ModelAdmin):
    list_display = ("pagetitle",)
    list_display_links = ("pagetitle",)
    form = WebsiteAdminForm

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("pagetitle",)
    list_display_links = ("pagetitle",)

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("pagetitle",)
    list_display_links = ("pagetitle",)


admin.site.register(Slider)
