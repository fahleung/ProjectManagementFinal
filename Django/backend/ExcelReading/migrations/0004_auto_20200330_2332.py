# Generated by Django 3.0.4 on 2020-03-30 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelReading', '0003_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courst',
            name='nom_cours',
            field=models.CharField(max_length=200),
        ),
    ]