from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.CharField(max_length = 1000, blank = True)

    def __str__(self):
        return self.user.username

class Photo(models.Model):
    image = models.ImageField(upload_to='uploaded_images', blank=True)
    title = models.CharField(max_length=128)
    # profile = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True)

    def delete_photo(self):
        self.delete()

    def update_photo(self):
        self.description = description
    
    def delete_url(self,photo_id):
        return reverse("delete", kwargs={"id" : photo_id})

    def get_absolute_url(self):
        return reverse("details", kwargs={"id" : self.id})

class Comment(models.Model):
    photo = models.ForeignKey(Photo)
    text = models.CharField(max_length=1000)