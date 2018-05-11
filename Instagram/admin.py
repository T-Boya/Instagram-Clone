from django.contrib import admin
from Instagram.models import UserProfile, Photo, Comment

admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(Comment)