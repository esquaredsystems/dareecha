# Generated by Django 4.1.6 on 2023-02-15 13:35

import baham.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baham', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('model_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=20)),
                ('model', models.CharField(default='Unknown', max_length=20)),
                ('type', models.CharField(choices=[('AUTO_RICKSHAW', 'Auto Rickshaw'), ('SEDAN', 'Sedan'), ('HATCHBACK', 'Hatch Back'), ('SUV', 'Sub-Urban Vehicle'), ('VAN', 'Van'), ('HIGH_ROOF', 'High Roof'), ('MOTORCYCLE', 'Moto cycle/Scooter')], help_text='Select the vehicle chassis type', max_length=50)),
                ('capacity', models.PositiveSmallIntegerField(default=2)),
            ],
            options={
                'db_table': 'baham_vehicle_model',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('registration_number', models.CharField(help_text='Unique registration/license plate no. of the vehicle.', max_length=10, unique=True)),
                ('colour', models.CharField(default='white', max_length=50, validators=[baham.models.validate_colour])),
                ('date_added', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('FULL', 'Full'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], max_length=50)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.vehiclemodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('type', models.CharField(choices=[('OWNER', 'OWNER'), ('COMPANION', 'COMPANION')], max_length=10)),
                ('primary_contact', models.CharField(max_length=20)),
                ('alternate_contact', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=255)),
                ('address_latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('address_longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('landmark', models.CharField(max_length=255)),
                ('town', models.CharField(choices=[('Bin Qasim', 'Bin Qasim'), ('Gadap', 'Gadap'), ('Gulberg', 'Gulberg'), ('Gulshan-e-Iqbal', 'Gulshan-e-Iqbal'), ('Jamshed', 'Jamshed'), ('Keamari', 'Keamari'), ('Korangi', 'Korangi'), ('Landhi', 'Landhi'), ('Liaquatabad', 'Liaquatabad'), ('Malir', 'Malir'), ('New Karachi', 'New Karachi'), ('North Nazimabad', 'North Nazimabad'), ('Orangi', 'Orangi'), ('SITE', 'SITE'), ('Saddar', 'Saddar'), ('Shah Faisal', 'Shah Faisal')], max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('date_deactivated', models.DateTimeField(editable=False, null=True)),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
