from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import redirect
from .models import User
from django.contrib import messages
# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Account has been registered successfully")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm

    context = {
        'form': form,
    }
    return render(request, 'accounts/register_user.html', context=context)


def register_restaurant(request):
    pass