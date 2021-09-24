
# Models
from django.contrib.auth.models import User
from users.models import Profile

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
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
    
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        })
    )


class ProfileInline(admin.StackedInline):
    """profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'

    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
