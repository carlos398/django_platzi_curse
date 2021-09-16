
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
    search_fields = (
        'user__email', 
        'user__username',
        'user__first_name', 
        'user__last_name', 
        'phone_number'
        )
    
    list_filter = (
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff'
        )