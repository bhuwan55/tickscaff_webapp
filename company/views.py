from django.shortcuts import render, redirect
from .models import Company

# Create your views here.

def AddCompany(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        try:
            image = request.FILES['image']
        except:
            image = request.POST.get("image")

        company = Company.objects.create(name=name, address=address, image=image)
        company.save()
        return redirect('company:view_company')

    return render(request,'addcompany.html',{})


def ViewCompany(request):
    company = Company.objects.all()
    return render(request, 'viewcompany.html', {'company':company})


def EditCompany(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        try:
            image = request.FILES['image']
        except:
            image = request.POST.get("image")

        company.name = name
        company.address = address
        company.image = image
        company.save()

    return render(request, 'editcompany.html', {'company': company})


def DeleteCompany(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('company:view_company')