from django.contrib import admin
from .models import Contributor

@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['name']