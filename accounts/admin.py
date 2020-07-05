from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(Images, ImagesAdmin)
admin.site.register(Profile, ProfileAdmin)
