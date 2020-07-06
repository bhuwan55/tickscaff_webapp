from django.shortcuts import render, redirect
from .models import Company

# Create your views here.

def AddCompany(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        site = request.POST.get("site")
        date_of_installation = request.POST.get("date_of_installation")

        company = Company.objects.create(name=name, site=site, date_for_installation=date_of_installation)
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
        site = request.POST.get("site")
        date_for_installation = request.POST.get("date_of_installation")

        if date_for_installation:
            company.date_for_installation = date_for_installation

        company.name = name
        company.site = site
        company.save()
        return redirect('company:view_company')

    return render(request, 'editcompany.html', {'company': company})


def DeleteCompany(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('company:view_company')