# Generated by Django 3.1.6 on 2021-02-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvbase', '0017_auto_20210217_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvbase',
            name='quarter',
        ),
    ]
