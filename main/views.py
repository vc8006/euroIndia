from django.shortcuts import render
from .models import User
from euroIndia.settings import STATIC_URL

def home(request):
    try:
        name = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        usr = User(name=name,email=email,phone=phone)
        try:
            usr.save()
        except:
            pass
    except:
        pass
    return render(request, "index.html",{"STATIC_URL":STATIC_URL})
