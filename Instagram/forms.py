from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from Instagram.models import UserProfile, Photo, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {'username': None,}
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username', 'class' : 'input'}),
        'password': forms.TextInput(attrs={'placeholder': 'Password', 'class' : 'input'}),
        'email': forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'input',}),

        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class PhotoForm(forms.ModelForm):
    image = forms.FileField(label='Select an image file', help_text='Please select a photo to upload')
    title = forms.CharField(max_length=128, help_text="Please enter the title of the photo.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    description = forms.CharField(max_length=1000, help_text="Please enter the description of the photo.")

    class Meta:
        model = Photo
        fields = ('image', 'title', 'description',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

class DetailUpdateForm(forms.ModelForm):
    description = forms.CharField(max_length=1000, help_text="Please enter the description of the photo.")

    class Meta:
        model = Photo
        fields = ('description',)
        exclude = ('profile', 'image', 'title', )

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=1000, help_text="Please enter your comment")

    class Meta:
        model = Comment
        fields = ('comment',)
        
    