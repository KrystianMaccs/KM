# Generated by Django 3.2.16 on 2023-02-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230218_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='John Doe', max_length=50),
        ),
    ]
