
# Models
from django.contrib.admin.decorators import display
from users.models import Profile

#Django
from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin."""

    list_display = ('user', 'phone_number', 'website', 'picture')