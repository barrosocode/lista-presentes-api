# Generated by Django 5.1.6 on 2025-03-01 17:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convidado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('link', models.CharField(max_length=150)),
                ('store', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presente_Convidado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lista_presentes_api.convidado')),
                ('presente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lista_presentes_api.presente')),
            ],
        ),
    ]
