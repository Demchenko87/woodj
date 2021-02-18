from django.db import models

class Csvbase(models.Model):
    date = models.CharField("Дата", max_length=150, blank=True, null=True)
    numb_lot = models.CharField("№ лоту", max_length=150, blank=True, null=True)
    p_lot = models.CharField("П/лот", max_length=150, blank=True, null=True)
    seller = models.CharField("Продавець", max_length=150, blank=True, null=True)
    product_name = models.CharField("Продукція", max_length=150, blank=True, null=True)
    product_type = models.CharField("Порода", max_length=150, blank=True, null=True)
    product_kind = models.CharField("Гатунок", max_length=150, blank=True, null=True)
    product_diameter = models.CharField("Діаметр (см)", max_length=150, blank=True, null=True)
    product_length = models.CharField("Довжина (м)", max_length=150, blank=True, null=True)
    storehouse = models.CharField("Склад", max_length=150, blank=True, null=True)
    product_size = models.CharField("Об'єм (м3)", max_length=150, blank=True, null=True)
    start_product_price = models.CharField("Початкова ціна (куб.м.)", max_length=150, blank=True, null=True)
    start_lot_price = models.CharField("Початкова ціна (лот)", max_length=150, blank=True, null=True)
    end_product_price = models.CharField("Продажна ціна (куб.м.)", max_length=150, blank=True, null=True)
    end_lot_price = models.CharField("Продажна ціна (лот)", max_length=150, blank=True, null=True)
    buyer = models.CharField("Найменування покупця", max_length=150, blank=True, null=True)
    EDRPOU = models.CharField("код ЄДРПОУ", max_length=150, blank=True, null=True)
    PDV_certificate = models.CharField("№ свідоцтва плати ПДВ", max_length=150, blank=True, null=True)
    IPN = models.CharField("Інд. Податковий номер (ІПН)", max_length=150, blank=True, null=True)
    buyer_address = models.CharField("Юр.адреса", max_length=150, blank=True, null=True)
    contact = models.CharField("Телефони", max_length=150, blank=True, null=True)
    commission = models.CharField("комісійний збір", max_length=150, blank=True, null=True)

    def __str__(self):
        return self.numb_lot
    class Meta:
        verbose_name = "CSV"
        verbose_name_plural = "Выгрузка CSV"


class Agrhouse(models.Model):
    name = models.CharField("Назва підприємства", max_length=150, blank=True, null=True)
    director = models.CharField("в особі керівника", max_length=150, blank=True, null=True)
    fio = models.CharField("Керівник ПІП", max_length=150, blank=True, null=True)
    statut = models.CharField("на підставі", max_length=150, blank=True, null=True)
    cod = models.CharField("КОД", max_length=150, blank=True, null=True)
    number_pdv = models.CharField("№свідоцтва плати ПДВ", max_length=150, blank=True, null=True)
    individual_number = models.CharField("Інд.подат. номер", max_length=150, blank=True, null=True)
    adress = models.CharField("Юридична адреса", max_length=150, blank=True, null=True)
    mailing_address = models.CharField("Поштова адреса", max_length=150, blank=True, null=True)
    score = models.CharField("Рахунок", max_length=150, blank=True, null=True)
    phone = models.CharField("ТЕЛЕФОНИ", max_length=150, blank=True, null=True)
    email = models.CharField("E-Mail", max_length=150, blank=True, null=True)
    region = models.CharField("Назва підприємства", max_length=150, blank=True, null=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сельхозы"
        verbose_name_plural = "Список сельхозов"

