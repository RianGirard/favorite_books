from django.shortcuts import render, redirect
import bcrypt, re
from .models import User
from django.contrib import messages


def index(request):

    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        if len(User.objects.filter(email=request.POST['email'])) == 0:
            messages.error(request, "Please enter a valid email and password")
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])[0]
        if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
            request.session['user_id'] = this_user.id
            # could add here ~  messages.success(request, "whatever")
            return redirect('/success')
        messages.error(request, "Please enter a valid email and password")
    return redirect('/')


def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    elif request.method == "POST":
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            fname=request.POST['first_name'],
            lname=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['user_id']= new_user.id
        # could add here ~  messages.success(request, "whatever")
        return redirect('/success')
    return redirect('/')


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return redirect('books/')

# -------------------------------------------------------------------------------------------------
# AJAX validators: 

def email_valid_null(request):
    # this is here to deal with null text entry cases
    found = 3
    return render(request, 'partials/email.html', {"found":found})

def email_valid(request, email):
    list = User.objects.filter(email=email)
    found = 2
    if len(list) > 0:
        found = 1
    return render(request, 'partials/email.html', {"found":found})      # found must be a dict datatype

def email_regex_null(request):
    # this is here to deal with null text entry cases
    found = 6
    return render(request, 'partials/email.html', {"found":found})

def email_regex(request, email):
    found = 4
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if EMAIL_REGEX.match(email):
        found = 5
    return render(request, 'partials/email.html', {"found":found})      # found must be a dict datatype
# ----------------------------------------------------------------------------------------------------



# Create your views here.
