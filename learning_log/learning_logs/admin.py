from django.contrib import admin

# Register your models here
# Encryting away some info from super_user

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
