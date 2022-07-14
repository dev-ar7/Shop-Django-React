from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'phone']


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)