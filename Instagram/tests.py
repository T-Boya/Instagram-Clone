from django.test import TestCase
from .models import Profile, Image, Comment, Like



class ProfileTestClass(TestCase):

    def setUp(self):
        # Setup for test instances
        self.UserProfile = UserProfile(, bio='I am groot.')

    def test_instance(self):
        # test to check Profile instance
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        # test the save method for saving profiles
        self.UserProfile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles) > 0)

   
class PhotoTestClass(TestCase):

    def setUp(self):
        # Setup for test instances
        self.Photo = Photo(image='I pooped my pants', title='Last Weekend', description="Don't tell Sam, LOL",)

    def test_instance(self):
        # test to check Image instance
        self.assertTrue(isinstance(self.Photo, Image))

    def test_save_image(self):
        # test to save Image instance
        self.Photo.save_image()
        Photos = Photo.objects.all()
        self.assertTrue(len(Photos) > 0)