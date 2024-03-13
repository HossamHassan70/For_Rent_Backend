# Generated by Django 5.0.3 on 2024-03-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SL_No', models.CharField(max_length=10)),
                ('Building_No', models.CharField(max_length=10)),
                ('Type', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('Availability', models.BooleanField(default=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Image', models.ImageField(upload_to='property_images/')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Rooms', models.IntegerField()),
                ('Bathrooms', models.IntegerField()),
            ],
        ),
    ]