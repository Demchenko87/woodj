# Generated by Django 3.1.6 on 2021-02-08 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvbase', '0010_addcsv_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcsv',
            name='date',
        ),
    ]
