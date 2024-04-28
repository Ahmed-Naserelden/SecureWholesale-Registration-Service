from django.contrib import admin
from .models import Organizations, Customers
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Organizations)
admin.site.register(Customers)