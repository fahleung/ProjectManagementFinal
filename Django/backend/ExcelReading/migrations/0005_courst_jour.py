# Generated by Django 3.0.4 on 2020-03-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelReading', '0004_auto_20200330_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='courst',
            name='jour',
            field=models.CharField(max_length=200, null=True),
        ),
    ]