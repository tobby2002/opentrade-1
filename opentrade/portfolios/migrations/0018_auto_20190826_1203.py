# Generated by Django 2.2.4 on 2019-08-26 12:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0017_auto_20190826_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
