from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OptCode
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login', )

    fieldsets = (
        ('ChangeUser', {'fields': ('email', 'fullname', 'phone_number', 'password')}),
        ('Permission', {'fields': ('is_admin', 'is_active', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ('CreateUser', {'fields': ('email', 'fullname', 'phone_number', 'password1', 'password2')}),
    )

    search_fields = ('email', 'fullname')
    ordering = ('fullname',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form


admin.site.register(User, UserAdmin)


@admin.register(OptCode)
class OptCodeAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'created')