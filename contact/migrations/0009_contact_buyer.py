# Generated by Django 3.1.6 on 2021-02-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20210208_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='buyer',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Найменування підприємства'),
        ),
    ]