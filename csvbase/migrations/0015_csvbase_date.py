# Generated by Django 3.1.6 on 2021-02-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvbase', '0014_delete_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvbase',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
