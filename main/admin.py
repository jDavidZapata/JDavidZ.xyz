from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User

# Register your models here.

admin.site.site_header = "JDavidZ.com's Site Administration"
admin.site.site_title = "JDavidZ.com"
admin.site.index_title = "Admin"

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass