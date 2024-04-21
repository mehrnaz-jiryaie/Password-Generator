from django.shortcuts import render, redirect
from .forms import PasswordForm
from .generator import generate_password
from .models import Password

def index(request):
    # Home Page
    return render(request, 'Pass_gen/home_page.html')


def password_view(request):
    password = ''
    if request.method == 'POST':
        form = PasswordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pass_gen:password')
    else:
        form = PasswordForm()
        # Generate password for initial rendering of the form
        # password_length = form.fields['password_length']
        try:
            last_password = Password.objects.latest('id')
            # id = last_password.id
            # password = Password.objects.get(id=id)
            password_length = last_password.password_length
            password = generate_password(password_length)
        # Do something with the ID
        except Password.DoesNotExist:
    # Handle the case where there are no objects in the database
            id = None 
        
    return render(request, 'Pass_gen/password.html', {'form': form, 'password': password})
