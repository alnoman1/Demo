from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User


# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def ceaser(request):
    return render(request, 'html/ceaser.html')

def hill(request):
    return render(request, 'html/hill.html')

def vernam(request):
    return render(request, 'html/vernam.html')

def transportation(request):
    return render(request, 'html/transportation.html')

def file(request):
    return render(request, 'html/file.html')

def image(request):
    return render(request, 'html/image.html')

def video(request):
    return render(request, 'html/video.html')

def blog(request):
    return render(request, 'html/blog.html')

#login..............
def indexx(request):
    return render(request, 'html/login.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def loginn(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'html/success.html', context)