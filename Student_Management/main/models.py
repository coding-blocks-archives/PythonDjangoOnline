from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length = 256)
  roll_number = models.IntegerField(unique = True)
  college = models.ForeignKey('College', on_delete = models.CASCADE)

  def __str__(self):
    return self.name

class College(models.Model):
  name = models.CharField(max_length = 256)

  def __str__(self):
    return self.name
