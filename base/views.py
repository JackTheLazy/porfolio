from django.shortcuts import render
from .models import Contact, Education, Whatiknow, Email,Address




# Create your views here.

def home(request):

    WIKvar = Whatiknow.objects.all()
    contactvar = Contact.objects.all()
    emailvar = Email.objects.all()
    addressvar = Address.objects.all()
    educationvar = Education.objects.all()

    return render(request,'base/home.html' ,{'WIKvar':WIKvar,'contactvar':contactvar,'emailvar':emailvar,'addressvar':addressvar,'educationvar':educationvar})