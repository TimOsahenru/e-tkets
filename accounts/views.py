from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, UserRegisterationForm
from django.urls import reverse
from django.contrib.auth import login, authenticate
from accounts.models import Profile
from events.models import Event


@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    events = Event.objects.filter(event_creator=request.user)

    context = {
        'active_page': 'profile',
        'user_profile': user_profile,
        'events': events,
    }
    return render(request, 'profile.html', context)


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request,
#                 email=cd['email'],
#                 password=cd['password'],
#                 backend='accounts.authentication.EmailAuthBackend'  # Specify your backend
#             )

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Diabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user) #unittest this
            return redirect('login')
            # return redirect ('profile')
            # return render(request, 'register_done_html', {'new_user': new_user})
        
    else:
        user_form = UserRegisterationForm()

    return render(request, 'register.html', {'user_form': user_form})



def custom_404_view(request, exception):
    return render(request, '404.html', status=404)