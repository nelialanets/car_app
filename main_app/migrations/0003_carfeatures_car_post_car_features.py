# Generated by Django 4.0.3 on 2022-04-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_car_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extras', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='car_post',
            name='car_features',
            field=models.ManyToManyField(to='main_app.carfeatures'),
        ),
    ]