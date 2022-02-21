from django.contrib import admin

# Register your models here.
from .models import Course # relative import -> models and admin are in the same directory

admin.site.register(Course)