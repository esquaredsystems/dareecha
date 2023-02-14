from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models

from baham.constants import COLOURS, CHOICES
from baham.enum_types import VehicleType, VehicleStatus, UserType


# Custom validators
def validate_color(value):
    '''
    Validate that the value exists in the list of available colors
    '''
    return value.upper() in COLOURS


# Create your models here.
class VehicleModel(models.Model):
    model_id = models.AutoField(primary_key=True, db_column='id')
    vendor = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False, default='Unknown')
    type = models.CharField(max_length=50, choices=[(t.name, t.value) for t in VehicleType],
                            help_text="Select the vehicle chassis type")
    capacity = models.PositiveSmallIntegerField(null=False, default=2)

    class Meta:
        db_table = "baham_vehicle_model"

    def __str__(self):
        return f"{self.vendor} {self.model}"


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True, db_column='id')
    registration_number = models.CharField(max_length=10, unique=True, null=False, blank=False,
                                           help_text="Unique registration/license plate no. of the vehicle.")
    color = models.CharField(max_length=50, default='white', validators=[validate_color])
    model = models.ForeignKey(VehicleModel, null=False, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date_added = models.DateField(default=now, editable=False)
    status = models.CharField(max_length=50, choices=[(t.name, t.value) for t in VehicleStatus])

    def __str__(self):
        return f"{self.model.vendor} {self.model.model} {self.color}"


class UserProfile(models.Model):
    # Should have one-to-one relationship with a Django user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    type = models.CharField(max_length=10, choices=[(t.name, t.value) for t in UserType])
    primary_contact = models.CharField(max_length=20, null=False, blank=False)
    alternate_contact = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255)
    address_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    address_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    landmark = models.CharField(max_length=255, null=False)
    town = models.CharField(max_length=50, null=False, choices=[(c, c) for c in CHOICES])
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True, editable=False)
    date_deactivated = models.DateTimeField(editable=False, null=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
