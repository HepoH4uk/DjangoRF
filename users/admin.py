from django.contrib import admin

from users.models import User, Payment

admin.site.register(Payment)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")