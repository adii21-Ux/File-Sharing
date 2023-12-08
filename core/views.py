from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth  import authenticate,  login as auth_login, logout


# Create your views here.
def home(request):
    return render(request, 'user/home.html')

def login(request):
    error_message = None

    if request.method == "POST":
        # Get the post parameters
        username = request.POST['uname']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials. Please try again."

    return render(request, 'auth/login.html', {'error_message': error_message})

def register(request):
    error_message = None

    if request.method == "POST":
        # Get the post parameters
        username = request.POST['uname']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        # Check for erroneous input
        if pass1 != pass2:
            error_message = "Passwords do not match. Please try again."
        else:
            # Create the user
            try:
                myuser = User.objects.create_user(username=username, password=pass1)
                myuser.save()
                return redirect('login')
            except Exception as e:
                error_message = f"An error occurred: {e}"

    return render(request, 'auth/register.html', {'error_message': error_message})