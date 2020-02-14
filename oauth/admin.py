from django.contrib import admin
from .models import User
# Register your models here.
from oauth import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'c_time', 'has_confirmed']


admin.site.register(models.User)
admin.site.register(models.ConfirmString)
