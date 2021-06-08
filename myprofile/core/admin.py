from django.contrib import admin

from core.models import Profile, Email


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )
