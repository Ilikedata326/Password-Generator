from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'passwordApp/home.html')

def about(request):
    return render(request, 'passwordApp/about.html')


def password(request):
    chars = "abcdefghijklmnopqrstuvwxyz"
    special_chars = "&@?!/\.^*()=#{$%µ€}" 
    characters = list(chars)
    
    if request.GET.get("uppercase"):
        characters.extend(chars.upper())
    
    if request.GET.get("special-characters"):
        characters.extend(list("&@?!/\.^*()=#{$%µ€}"))
    
    if request.GET.get("numbers"):
        characters.extend(list('0123456789'))
        
    length = int(request.GET.get("length", 12))
    
    password = ''
    for x in range(length):
        password += random.choice(characters)
    
    context = {
        'password':password,
    }
    return render(request, 'passwordApp/password.html', context)