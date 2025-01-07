from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_verified', 'joined_at')
    list_filter = ('is_staff', 'is_active', 'is_verified', 'college_year')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'avatar')}),
        ('Personal Info', {'fields': ('bio', 'phone_number', 'college_year', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'is_staff', 'is_active', 'is_verified')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
