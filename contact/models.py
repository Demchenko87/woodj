from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField("e-mail", max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    login = models.CharField("Логин", max_length=150)
    password = models.CharField("Пароль", max_length=150)
    fio = models.CharField("ФИО", max_length=150)
    phone = models.CharField("Телефон", max_length=150)
    edrpo = models.CharField("ЄДРПОУ", max_length=150)

    message = models.TextField("Информация про участника")

    def __str__(self):
        return self.email


class Head(models.Model):
    firma = models.CharField("назва фiрми", max_length=150)
    adress = models.CharField("адреса фiрми", max_length=150)
    phone = models.CharField("телефон фiрми", max_length=150)
    site = models.CharField("сайт фiрми", max_length=150)
    director = models.CharField("директор фiрми", max_length=150)
    fio = models.CharField("ПIБ", max_length=150)

    def __str__(self):
        return self.firma
