# Generated by Django 4.1.7 on 2023-02-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_profile_city_profile_number_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='profile',
            name='post_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=50),
        ),
    ]
