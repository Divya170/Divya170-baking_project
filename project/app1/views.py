from django.shortcuts import render
from app1.models import table
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mn']
        address=request.POST['address']
        mail=request.POST['email']
        feedback=request.POST['fb']
        table.objects.create(name=name,mn=mobile,address=address,email=mail,feedback=feedback)

    return render(request,"index.html")

