# Generated by Django 3.1.6 on 2021-02-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvbase', '0008_addcsv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcsv',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
