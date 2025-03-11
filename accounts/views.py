from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, UserRegisterationForm
from django.urls import reverse
from django.contrib.auth import login, authenticate


def profile(request):
    return HttpResponse()


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
            return redirect ('profile')
            # return render(request, 'register_done_html', {'new_user': new_user})
        
    else:
        user_form = UserRegisterationForm()

    return render(request, 'register.html', {'user_form': user_form})