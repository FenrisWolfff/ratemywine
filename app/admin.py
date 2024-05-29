from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.

app = apps.get_app_config('app')

for _, model in app.models.items():
    admin.site.register(model)
