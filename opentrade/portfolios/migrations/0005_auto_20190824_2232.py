# Generated by Django 2.2.4 on 2019-08-24 22:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_auto_20190824_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='ident',
            field=models.UUIDField(default=uuid.UUID('d0cae747-ca5b-4bb8-af84-add1f3fe75a1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
