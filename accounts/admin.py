from django.contrib import admin
from accounts.models import UserRole

from accounts.views import register
from .models import Role, UserRole

admin.site.register((Role, UserRole))
