from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0) , MaxValueValidator(80)])
    job_title = models.CharField(max_length=100)
    address = models.TextField()