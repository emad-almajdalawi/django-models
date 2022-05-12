from django.contrib import admin
from .models import Snack

# class AdminSnack(admin.ModelAdmin):
#     pass

admin.site.register(Snack)