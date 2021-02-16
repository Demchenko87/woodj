from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email","login","password","fio","phone","edrpo", "message", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder":"email",}),
            "login": forms.TextInput(attrs={"class": "form-control", "placeholder":"Логiн",}),
            "password": forms.TextInput(attrs={"class": "form-control", "placeholder":"Пароль"}),
            "fio": forms.TextInput(attrs={"class": "form-control", "placeholder":"ПIБ"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder":"Телефон"}),
            "edrpo": forms.TextInput(attrs={"class": "form-control", "placeholder": "ЄДРПОУ"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder":"Iнформацiя"})
        }
