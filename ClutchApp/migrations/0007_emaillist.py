# Generated by Django 3.1.5 on 2021-02-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClutchApp', '0006_shippingaddress_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
