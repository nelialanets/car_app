# Generated by Django 4.0.3 on 2022-04-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_carfeatures_car_post_car_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='carfeatures',
            name='interior',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carfeatures',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carfeatures',
            name='roof_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carfeatures',
            name='transmtion_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
