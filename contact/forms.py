from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email", "login", "password", "name", "fio", "phone", "edrpo", "ipn", "r_r", "adress",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder":"email",}),
            "login": forms.TextInput(attrs={"class": "form-control", "placeholder":"Логiн",}),
            "password": forms.TextInput(attrs={"class": "form-control", "placeholder":"Пароль"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Назва пiдприємства"}),
            "fio": forms.TextInput(attrs={"class": "form-control", "placeholder":"ПIБ"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder":"Телефон"}),
            "edrpo": forms.TextInput(attrs={"class": "form-control", "placeholder": "ЄДРПОУ"}),
            "ipn": forms.TextInput(attrs={"class": "form-control", "placeholder": "IПН"}),
            "r_r": forms.TextInput(attrs={"class": "form-control", "placeholder": "р/р"}),
            "adress": forms.TextInput(attrs={"class": "form-control", "placeholder": "adress"}),
        }
