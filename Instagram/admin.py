from django.contrib import admin
from Instagram.models import UserProfile, Photo, Comment, Follow, Like

admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)