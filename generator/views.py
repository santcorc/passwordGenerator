from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import secrets

def root(request):
    return redirect('home/')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


def password(request):

    characters = list('qwertyuiopasdfghjklñzxcvbnm')

    numbers = list('1234567890')

    specialCharacters = list('!"·$%&/=?}@')

    randomPassword = ''

    

    lengthPassword = request.GET.get('length')

    try:
        lengthPassword=int(lengthPassword)
    except:
        if (lengthPassword==''):
            messages.error(request,'length cannot be empty')
            return redirect('home/')
        else:
            messages.error(request,'length must be a number')
            return redirect('home/')
        
    
    if (lengthPassword<8):
        messages.error(request,'length must be 8 or more')
        return redirect('home/')

    isUppercase = False

    if (request.GET.get('criptographicstrongpassword')):
        randomPassword = secrets.token_urlsafe(lengthPassword)
        return render (request, 'password.html', {'password': randomPassword})

    if (request.GET.get('uppercase')):
        isUppercase = True

    if (request.GET.get('numbers')):
        characters.extend(numbers)

    if (request.GET.get('specialCharacters')):
        characters.extend(specialCharacters)
    
    if (isUppercase):
        for i in range(lengthPassword):
            k = secrets.randbelow(2)
            if (k):
                randomPassword+=secrets.choice(characters).upper()
            else :
                randomPassword+=secrets.choice(characters)

       
    
    else:
        for i in range(lengthPassword):
            randomPassword+=secrets.choice(characters)

    return render(request, 'password.html', {'password': randomPassword})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"