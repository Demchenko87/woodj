from django.db import models
# Main page begin
class Slider(models.Model):
    active = models.CharField("Первый слайдер", max_length=150, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="slider/")
    pagetitle = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Описание")
    def __str__(self):
        return self.pagetitle
    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class AboutUs(models.Model):
    content = models.TextField("Описание")
    def __str__(self):
        return self.content
    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "О компании"


class Services(models.Model):
    image = models.ImageField("Изображение", upload_to="services/")
    pagetitle = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.pagetitle
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Partners(models.Model):
    image = models.ImageField("Изображение", upload_to="partners/")
    pagetitle = models.CharField("Заголовок", max_length=150)

    def __str__(self):
        return self.pagetitle
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
# main page end

# auctions page
class Auctions(models.Model):
    pagetitle = models.CharField("Заголовок", max_length=150, blank=True, null=True)
    content = models.TextField("Аукционы", blank=True, null=True )
    def __str__(self):
        return self.pagetitle
    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Аукционы"
# end auctions page

