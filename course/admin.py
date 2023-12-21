from django.contrib import admin
from . import models


@admin.register(models.Students)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "instructor",
        "capacity",
        "open_seats",
    )
