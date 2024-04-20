from django.db import models
from django.core.exceptions import ValidationError

def validate_non_zero(value):
    if value == 0:
        raise ValidationError('Value cannot be zero.')

class UnsignedNonZeroIntegerField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_non_zero]
        super().__init__(*args, **kwargs)
