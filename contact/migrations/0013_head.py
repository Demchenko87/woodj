# Generated by Django 3.1.6 on 2021-02-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_remove_contact_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma', models.CharField(max_length=150, verbose_name='назва фiрми')),
                ('adress', models.CharField(max_length=150, verbose_name='адреса фiрми')),
                ('phone', models.CharField(max_length=150, verbose_name='телефон фiрми')),
                ('site', models.CharField(max_length=150, verbose_name='сайт фiрми')),
                ('director', models.CharField(max_length=150, verbose_name='директор фiрми')),
                ('fio', models.CharField(max_length=150, verbose_name='ПIБ')),
            ],
        ),
    ]
