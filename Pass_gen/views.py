from django.shortcuts import render, redirect
from .forms import PasswordForm
from .generator import generate_password
from .models import Password

def index(request):
    # Home Page
    return render(request, 'Pass_gen/home_page.html')


def password_view(request):
    password = None
    if request.method == 'POST':
        form = PasswordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pass_gen:password')
    else:
        form = PasswordForm()
        # Generate password for initial rendering of the form
        password_length = form.fields['password_length']
        password = generate_password(password_length)
    return render(request, 'Pass_gen/password.html', {'form': form, 'password': password})
