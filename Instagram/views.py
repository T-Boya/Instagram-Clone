from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Instagram.forms import UserForm, UserProfileForm, PhotoForm, DetailUpdateForm
from Instagram.models import Photo, UserProfile

def index(request):
    return render(request, 'Instagram/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'Instagram/register.html', {'user_form': user_form, 'profile_form': profile_form,'registered': registered})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'Instagram/login.html', {})
        # ADD ERROR MESSAGES

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# @login_required
# def index(request):
#     return render(request, 'Instagram/index.html', )

@login_required
def images(request):
        photos = Photo.objects.all()
        return render(request, 'Instagram/view_images.html', context = {'photos' : photos,})

@login_required
def upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # photo = form.save(commit=False)
            photo = Photo(image = request.FILES['image'])
            photo.save()
            return HttpResponseRedirect(reverse('images'))
    else:
        print(form.errors)
    return render(request, 'Instagram/upload.html', context = {'form':form,})

@login_required
def details(request, id = None):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'Instagram/details.html', context = {'photo' : photo,})

def deleteImage(request, photo_id):
    image = Photo.objects.filter(id=photo_id).first()
    image.delete_photo()
    return redirect('images')

@login_required
def search(request, id=None):
    User = get_object_or_404(UserProfile, id=id) #FIGURE OUT HOW TO INSERT SEARCH QUERY AFTER USER
    return render(request, 'Instagram/search.html', context = {'instance':instance,})

@login_required
def update(request, photo_id):
    update_photo(self)
    image = Photo.objects.filter(id=photo_id).first()
    image.update_photo(description = description)
    # instance = get_object_or_404(Photo, id=id)
    # form = DetailUpdateForm(instance=instance)
    # if form.is_valid():
    #     # description = request.POST.get('description')
    #     form.save()
    #     return HttpResponseRedirect(reverse('images'))
    # else:
    #     print(form.errors)
    return render(request, 'Instagram/update.html', context = {'instance' : instance, 'form':form,})

    