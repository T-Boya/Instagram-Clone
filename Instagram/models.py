from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from annoying.fields import AutoOneToOneField
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.CharField(max_length = 1000, blank = True)
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    # @classmethod
    # def follows(id):
    #     followee = get_object_or_404(UserProfile, id=id)
    #     add_follower = current_user.follows.add(user)
    #     request.user.follows.add(followee)
#         photo = cls.objects.filter(title__icontains=query)
#         return photo
    
    # instance = UserProfile.objects.get(id)
    # photos = instance.photo_set.all()

    def __str__(self):
        return self.user.username

    # def photos(self):
    #     return self.objects.get(self).photo_set.all()

# class Category(models.Model):
#     title = models.CharField(max_length = 128)

class Comment(models.Model):
    text = models.CharField(max_length=1000, blank=True, default='nice!')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)

class Photo(models.Model):
    image = models.ImageField(upload_to='uploaded_images', blank=True)
    title = models.CharField(max_length=128)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='likes')
    description = models.CharField(max_length=1000, blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    # category = models.ForeignKey(Category, blank = True)

    # @property
    # def total_likes(self):
    #     return self.likes.count()

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
