from django.core.exceptions import ValidationError

def validate_even_number(value):
  if value % 2:
    raise ValidationError("Given value is not even")
