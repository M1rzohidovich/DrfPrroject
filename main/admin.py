from django.contrib import admin
from .models import Region, District, Announcement, Blog

admin.site.register((Region, District, Announcement, Blog))


