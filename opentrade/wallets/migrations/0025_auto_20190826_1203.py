# Generated by Django 2.2.4 on 2019-08-26 12:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0024_auto_20190826_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='ident',
            field=models.UUIDField(default=uuid.UUID('3556f2ae-0a78-4776-9303-7cb44e094894'), editable=False, primary_key=True, serialize=False),
        ),
    ]
