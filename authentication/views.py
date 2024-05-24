from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def auth_page(request):
    if request.method == 'POST':
        if 'password1' in request.POST:  # Registration form submission
            register_form = UserCreationForm(request.POST)
            login_form = AuthenticationForm()
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('authentication:auth_page')
        elif 'password' in request.POST:  # Login form submission
            login_form = AuthenticationForm(data=request.POST)
            register_form = UserCreationForm()
            if login_form.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    if user.is_superuser:
                        messages.success(request, 'You are now logged in as a superuser!')
                        return redirect('admin:admin_landing')
                    else:
                        messages.success(request, 'You are now logged in!')
                        return redirect('list_information:data_information')
                else:
                    messages.error(request, 'Invalid username or password')
    else:
        register_form = UserCreationForm()
        login_form = AuthenticationForm()

    return render(request, 'auth_page.html', {'register_form': register_form, 'login_form': login_form})

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('list_information:data_list')
