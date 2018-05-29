from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from annoying.fields import AutoOneToOneField
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = AutoOneToOneField('auth.user')
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.CharField(max_length = 1000, blank = True)

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    stalker = models.ForeignKey(User, related_name='stalker')
    victim = models.ForeignKey(User, related_name='vitctim')

class Photo(models.Model):
    image = models.ImageField(upload_to='uploaded_images', blank=True)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='likes')
    description = models.CharField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)

    def delete_photo(self):
        self.delete()

    def update_photo(self):
        self.description = description
    
    def delete_url(self,photo_id):
        return reverse("delete", kwargs={"id" : photo_id})

    def get_absolute_url(self):
        return reverse("details", kwargs={"id" : self.id})

    @classmethod
    def search(cls, query):
        photo = cls.objects.filter(title__icontains=query)
        return photo

class Comment(models.Model):
    text = models.CharField(max_length=1000, blank=True, default='nice!')
    author = models.ForeignKey(User)
    photo = models.ForeignKey(Photo)

class Follow(models.Model):
    stalker = models.ForeignKey(User, related_name='stalker')
    victim = models.ForeignKey(User, related_name='victim')

class Like(models.Model):
    liker = models.ForeignKey(User, related_name='liker')
    photo = models.ForeignKey(Photo, related_name='photo')
    liked = models.BooleanField(default=False)