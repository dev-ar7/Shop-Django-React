from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

PHONE_VALIDATORS = RegexValidator(
    r'\d{3}?-?\d{3}?-?\d{4}', 'Only numbers allowed.')


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=False, null=False,
                             validators=[PHONE_VALIDATORS])
    address = models.CharField(max_length=221, blank=False, null=False)
    city = models.CharField(max_length=75, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    zipcode = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
