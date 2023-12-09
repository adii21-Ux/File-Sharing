from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,  login as auth_login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import UploadedFile
from django.shortcuts import render, get_object_or_404


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
            return redirect('profile')
        else:
            error_message = "Invalid login credentials. Please try again."

    return render(request, 'auth/login.html', {'error_message': error_message})


def register(request):
    error_message = None

    if request.method == "POST":
        # Get the post parameters
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['uname']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        # Check for erroneous input
        if pass1 != pass2:
            error_message = "Passwords do not match. Please try again."
        else:
            # Create the user
            try:
                myuser = User.objects.create_user(
                    username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                myuser.save()
                return redirect('login')
            except Exception as e:
                error_message = f"An error occurred: {e}"

    return render(request, 'auth/register.html', {'error_message': error_message})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'user/profile.html', context)


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user/user_profile.html', {'profile_user': user})


@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('profile')
    else:
        form = FileUploadForm()
    return render(request, 'files/file_upload.html', {'form': form})


def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(
        uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response


@login_required
def file_list(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    shared_with_user_files = UploadedFile.objects.filter(
        shared_with=request.user)
    return render(request, 'files/file_list.html', {'user_files': user_files, 'shared_with_user_files': shared_with_user_files})


def search_profiles(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        results = []

        if query:
            results = User.objects.filter(username__icontains=query)

    return render(request, 'user/search_users.html', {'query': query, 'results': results})


@login_required
def share_file(request, file_id):
    file_to_share = get_object_or_404(UploadedFile, id=file_id)

    if request.method == 'POST':
        recipients = request.POST.getlist('recipients')
        file_to_share.shared_with.set(recipients)
        file_to_share.save()
        return redirect('file_list')

    all_users = User.objects.exclude(id=request.user.id)
    return render(request, 'share/share_file.html', {'file_to_share': file_to_share, 'all_users': all_users})
