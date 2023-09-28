from django.shortcuts import render
from datetime import datetime
from .models import Contact
from Care_Centre.models import MedicineData
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'Home-page.html')
def about(request):
    return render(request, 'about_us.html')
def search(request):
    return render(request, 'ayurvedic_treatment.html')
def result(request):
    # if request.method=="GET":
    st=request.POST.get('search')
    if st!=None:
        lookup = (Q(symptoms__icontains=st) | Q(name__icontains=st))
        sol = MedicineData.objects.filter(lookup)
        # sol = MedicineData.objects.filter(name__icontains=st)
    solu={
        'sol':sol
    }        
    #back_to_jason = JSON.stringify(js_data) 
    return render(request,'result.html', solu)
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        contact = Contact(person_name=name, email=email, phone=phone, desc=desc, date= date)
        contact.save()
    return render(request, 'Doctor_consultation.html')

def thanks(request):
    return render(request, 'thank_you.html')
