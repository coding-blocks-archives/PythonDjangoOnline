from django.contrib import admin
from relationship_playground import models

# Register your models here.

admin.site.register([
  models.Article,
  models.Author,
  models.Pizza,
  models.Topping,
  models.Person,
  models.Society,
  models.Membership
])
