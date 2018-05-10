from django.shortcuts import render
from django.http import HttpResponse
from Instagram.forms import UserForm, UserProfileForm

def index(request):
    return HttpResponse('Gaaaaaaaaaaay!')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.post)
        profile_form = UserProfileForm(data=request.post)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save
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

    return render(request, 'Instagram/register.html')