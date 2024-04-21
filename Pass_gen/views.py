from django.shortcuts import render, redirect
from .forms import PasswordForm
from .generator import generate_password
from .models import Password


def password_view(request):
    password = ''
    if request.method == 'POST':
        form = PasswordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pass_gen:password')
    else:
        form = PasswordForm()
        try:
            last_password = Password.objects.latest('id')
            password_length = last_password.password_length
            password = generate_password(password_length)
        except Password.DoesNotExist:
            id = None 
        
    return render(request, 'Pass_gen/password.html', {'form': form, 'password': password})
