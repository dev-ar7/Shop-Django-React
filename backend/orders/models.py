from django.db import models
from django.core.validators import RegexValidator


PHONE_VALIDATORS = RegexValidator(
    r'\d{3}?-?\d{3}?-?\d{4}', 'Only numbers allowed.')

PENDING = 'PND'
RETURN = 'RTN'
COMPLETED = 'CMPL'
STATUS = [
    (PENDING, 'Pending'),
    (RETURN, 'Return'),
    (COMPLETED, 'Completed'),
]

class Order(models.Model):

    cart = models.JSONField(encoder=None, blank = False, null=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=15, blank=False,
                             null=True, validators=[PHONE_VALIDATORS])
    address = models.CharField(max_length=221, blank=False, null=False)
    city = models.CharField(max_length=75, blank=False, null=False)
    state = models.CharField(max_length=20, blank=False, null=False)
    zipcode = models.CharField(max_length=10, blank=False, null=False)
    subtotal = models.CharField(max_length=10, blank=False, null=False)
    tax = models.CharField(max_length=10, blank=False, null=True)
    total = models.CharField(max_length=10, blank=False, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['status', 'created_at']

    def __str__(self):
        return f'{self.first_name} {self.id}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return '%s %s %s %s' % (self.address, self.city, self.state, self.zipcode)
    
    def phone_num(self):
        return f'{self.phone}'