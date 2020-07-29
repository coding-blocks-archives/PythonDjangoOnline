from django.contrib import admin
from social import models

# Register your models here.
admin.site.register([
  models.Post,
  models.Friends,
  models.Like
])
