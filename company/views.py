from django.shortcuts import render, redirect
from .models import Company
from main.models import Gear, Job

# Create your views here.

def AddCompany(request):
    if request.method == 'POST':
        company_name = request.POST.get("company_name")
        site = request.POST.get("job_site")
        builder_name = request.POST.get("builder_name")
        builder_abn = request.POST.get("builder_abn")
        sub_name = request.POST.get("sub_name")
        sub_contact = request.POST.get("sub_contact")
        amount_of_bays = request.POST.get("amount_of_bays")
        job_type = request.POST.get("job_type")
        job = Job.objects.create(site=site)
        job.save()
        company = Company(job=job, name=company_name,builder_name=builder_name,builder_abn=builder_abn,sub_name=sub_name,sub_contact=sub_contact,amount_of_bays=amount_of_bays,job_type=job_type)


        try:
            quote = request.FILES['quote']
            date_of_installation = request.POST.get("job_date_of_installation")
            company.quote = quote
            company.save()
            job.date_for_installation = date_of_installation
            job.save()

        except:
            quote = request.POST.get("quote")

        company.save()
        return redirect('main:new_add_jobs', id=job.id)

    return render(request,'addupdatecompany.html',{})


def ViewCompany(request):
    company = Company.objects.all()
    return render(request, 'viewcompany.html', {'company':company})


def EditCompany(request, id):
    company = Company.objects.get(id=id)
    job = Job.objects.get(id = company.job.id)
    orders = job.order.all().order_by("id")

    if request.method == "POST":
        company_name = request.POST.get("company_name")
        site = request.POST.get("job_site")
        builder_name = request.POST.get("builder_name")
        builder_abn = request.POST.get("builder_abn")
        sub_name = request.POST.get("sub_name")
        sub_contact = request.POST.get("sub_contact")
        amount_of_bays = request.POST.get("amount_of_bays")
        job_type = request.POST.get("job_type")
        sbtn = request.POST.get("sbtn")

        job.site = site
        job.save()

        company.name = company_name
        company.builder_name = builder_name
        company.builder_abn = builder_abn
        company.sub_name = sub_name
        company.sub_contact = sub_contact
        company.amount_of_bays = amount_of_bays
        company.job_type = job_type
        company.save()

        try:
            date_of_installation = request.POST.get("job_date_of_installation")
            print(date_of_installation)
            job.date_for_installation = date_of_installation
            job.save()
            quote = request.FILES['quote']
            company.quote = quote
            company.save()

        except:
            quote = request.POST.get("quote")

        company.save()
        if sbtn == "submit":
            return redirect('company:view_company')
        else:
            return redirect('main:edit_jobs', id=job.id)

    return render(request, 'editcompany.html', {'company': company, 'job': job , 'orders':orders})


def DeleteCompany(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    if company.job:
        return redirect('main:delete_jobs',id=company.job.id)
    else:
        return redirect('company:view_company')