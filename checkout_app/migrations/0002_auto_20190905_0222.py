# Generated by Django 2.2.4 on 2019-09-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
