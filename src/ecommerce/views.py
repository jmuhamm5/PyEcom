from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title' : 'Hello World',
        'content' : 'Welcome to the homepage.'
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEEAAAHHHH"
    return render(request, 'pages/home.html', context)

def about_page(request):
    context = {
        'title' : 'About Page',
        'content' : 'Welcome to the about page.'
    }
    return render(request, 'pages/about.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title' : 'Contact Page',
        'content' : 'Welcome to the contact page.',
        'form' : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'pages/contact.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }  
    #print(request.user.is_authenticated
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated
        if user is not None:
            #print(request.user.is_authenticated
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print('error')       
    return render(request, "pages/auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "pages/auth/register.html", context)