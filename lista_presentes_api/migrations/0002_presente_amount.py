# Generated by Django 5.1.6 on 2025-03-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_presentes_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presente',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
