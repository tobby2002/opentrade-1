# Generated by Django 2.2.4 on 2019-08-24 22:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('ident', models.UUIDField(default=uuid.UUID('19accd98-54e2-4e2a-8a60-31f51c610deb'), editable=False, primary_key=True, serialize=False)),
                ('init_amount', models.FloatField(default=40000.0)),
                ('amount', models.FloatField(default=40000.0)),
            ],
        ),
    ]