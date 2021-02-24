# Generated by Django 3.1.6 on 2021-02-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='adress',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Юр. адрес'),
        ),
        migrations.AddField(
            model_name='contact',
            name='ipn',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ІПН'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Назва пiдприємства'),
        ),
        migrations.AddField(
            model_name='contact',
            name='r_r',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='р/р'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='edrpo',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ЄДРПОУ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fio',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ПIБ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='login',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Додаткова iнформацiя про участника'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Телефон'),
        ),
    ]