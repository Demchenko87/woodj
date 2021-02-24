from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField("e-mail", max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    login = models.CharField("Логин", max_length=150, blank=True, null=True)
    password = models.CharField("Пароль", max_length=150, blank=True, null=True)
    name = models.CharField("Назва пiдприємства", max_length=150, blank=True, null=True)
    fio = models.CharField("ПIБ", max_length=150, blank=True, null=True)
    phone = models.CharField("Телефон", max_length=150, blank=True, null=True)
    edrpo = models.CharField("ЄДРПОУ", max_length=150, blank=True, null=True)
    ipn = models.CharField("ІПН", max_length=150, blank=True, null=True)
    r_r = models.CharField("р/р", max_length=150, blank=True, null=True)
    adress = models.CharField("Юр. адрес", max_length=150, blank=True, null=True)
    message = models.TextField("Додаткова iнформацiя про участника", blank=True, null=True)

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
