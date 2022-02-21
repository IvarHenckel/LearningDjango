from django.contrib import admin

# Register your models here.
from .models import Article # relative import -> models and admin are in the same directory

admin.site.register(Article)