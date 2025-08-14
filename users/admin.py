from django.contrib import admin

from users.models import User, Payment

admin.site.register(Payment)
admin.site.register(User)