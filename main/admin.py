from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User

# Register your models here.

admin.site.site_header = "JDavidZ.xyz's Site Administration"
admin.site.site_title = "JDavidZ.xyz"
admin.site.index_title = "Admin"

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass