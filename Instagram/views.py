from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Instagram.forms import UserForm, UserProfileForm, PhotoForm, DetailUpdateForm, CommentForm, FollowForm
from Instagram.models import Photo, UserProfile, Comment, Follow, Like
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST


# def index(request):
#     return render(request, 'Instagram/index.html')

def index(request):

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
            return HttpResponseRedirect(reverse('login'))

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
                return HttpResponseRedirect(reverse('images'))

            else:
                return HttpResponse("Your account is disabled.")

        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'Instagram/login.html')
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

    all_likes = Like.objects.all()
    # for photo in photos:
    #     pic_likes = all_likes.filter(photo_id=id)
    #     like_count = len(pic_likes)
    #     liker = pic_likes.filter(liker_id=request.user.id)
    #     if len(liker) != 0:
    #         liked=True
    # comments = Photo.comments.all()

    # instance = get_object_or_404(Photo, id=id)
    # form = CommentForm()
    # if request.method == 'POST':
    #     form = PhotoForm(request.POST)
    #     if form.is_valid():
    #         # photo = form.save(commit=False)
    #         instance.comment.text = request.POST.get('comment')
    #         instance.comment = form.save(commit=False)
    #         instance.comment.author = request.user
    #         instance.comment = comment.save()
    #         return HttpResponseRedirect(reverse('images'))
    # else:
    #     print(form.errors)

    return render(request, 'Instagram/view_images.html', context = {'photos' : photos,})

@login_required
def upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # photo = form.save(commit=False)
            photo = Photo(image = request.FILES['image'])
            photo = form.save(commit=False)
            photo.author = request.user
            photo = photo.save()
            return HttpResponseRedirect(reverse('images'))
    else:
        print(form.errors)
    return render(request, 'Instagram/upload.html', context = {'form':form,})

@login_required
def details(request, id = None):
    photo = get_object_or_404(Photo, id=id)
    form = CommentForm()
    liked=False
    all_likes = Like.objects.all()
    pic_likes = all_likes.filter(photo_id=id)
    like_count = len(pic_likes)
    liker = pic_likes.filter(liker_id=request.user.id)
    if len(liker) != 0:
        liked=True
    all_comments = Comment.objects.all().order_by('-id')
    comments = all_comments.filter(photo_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.photo = photo
            comment.save()
            return redirect('details', id=photo.id)
    else:
        form = CommentForm()
    return render(request, 'Instagram/details.html', context = {'form':form, 'comments':comments, 'photo':photo, 'form':form, 'like_count':like_count, 'liked':liked})

@login_required
def deleteImage(request, photo_id):
    image = Photo.objects.filter(id=photo_id).first()
    image.delete_photo()
    return redirect('images')

@login_required
def search(request):
    if 'title' in request.GET and request.GET["title"]:
        query = request.GET.get("title")
        print(query)
        photos = Photo.search(query)
        print(photos)
        output = f"{query}"
        print(output)

        return render(request,'Instagram/search.html',{"output":output, "photos":photos})

    else:
        message = "You haven't searched for anything"
        return render(request, 'Instagram/search.html',{"message":message})
    return render(request, 'Instagram/search.html',)

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

@login_required
def user(request, id=None):
    user = get_object_or_404(UserProfile, id=id)
    user_Photos = Photo.objects.filter(author_id=id)
    # photos = User_Photos.photo_set.all()
    photos = user_Photos.all()
    all_followers = Follow.objects.all()
    user_followers = all_followers.filter(victim_id=id)
    user_following = all_followers.filter(stalker_id=id)
    follow_count = len(user_followers)
    user_follow_count = len(user_following)
    if len(user_following) != 0:
        following = True
    all_likes = Like.objects.all()
    pic_likes = all_likes.filter(photo_id=id)
    like_count = len(pic_likes)
    liker = pic_likes.filter(liker_id=request.user.id)
    if len(liker) != 0:
        liked=True
    # Photo_comments = Comment.objects.filter(author_id=id).filter(photo_id=photo.id)
    # comments = Photo_comments.all()

    # current_user = request.user
    # add_follower = current_user.follows.add(user)
    return render(request, 'Instagram/user.html', context = {'photos' : photos, 'follow_count':follow_count, 'following':following, 'user':user,'like_count':like_count, 'liked':liked,})

# # @login_required
# @require_POST
# def like(request):
#     if request.method == 'POST':
#         user = request.user
#         slug = request.POST.get('slug', None)
#         company = get_object_or_404(Photo, slug=slug)

#         if photo.likes.filter(id=user.id).exists():
#             # user has already liked this company
#             # remove like/user
#             photo.likes.remove(user)
#             message = 'You disliked this'
#         else:
#             # add a new like for a company
#             photo.likes.add(user)
#             message = 'You liked this'

#     ctx = {'likes_count': photo.total_likes, 'message': message}
#     return HttpResponse(json.dumps(ctx), content_type='application/json')


@login_required
def follow(request, id = None):
    victim = get_object_or_404(UserProfile, id=id)
    follow = Follow(victim=victim.user, stalker=request.user)
    follow.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def like(request, id = None):
    photo = get_object_or_404(Photo, id=id)
    like = Like(liker=request.user, photo=photo, liked=True)
    like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))