# Generated by Django 5.0.3 on 2024-03-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('role', models.CharField(choices=[('Renter', 'Renter'), ('Owner', 'Owner'), ('Admin', 'Admin')], default='Renter', max_length=7)),
                ('validation_states', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]