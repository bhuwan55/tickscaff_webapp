from django.shortcuts import render, redirect
from .models import Invoice
from main.models import Job
from company.models import Company
from quote.models import Quote
import datetime
from datetime import timedelta
# Create your views here.


def CreateInvoice(request,id):
    quote = Quote.objects.get(id=id)
    total = quote.subtotal + quote.gst

    days = quote.hire_period * 7
    date_of_dismantle = quote.job.date_for_installation + datetime.timedelta(days=days)

    description1 = "Scaffold hire for " + str(quote.hire_period) + " weeks starting from, " + str(quote.job.date_for_installation) + " until " + str(date_of_dismantle) + "."

    invoice = Invoice.objects.create(quote=quote, subtotal1=quote.subtotal, gst1=quote.gst, total1=total\
                                     , date_of_dismantle=date_of_dismantle, subtotal=quote.subtotal\
                                     , gst=quote.gst, total=total, description1=description1)
    invoice.save()
    today = datetime.date.today()
    return redirect('invoice:view_single_invoice', invoice.id)


def ViewSingleInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    return render(request, 'viewsingleinvoice.html', {'invoice': invoice, })


def ViewAllInvoice(request):
    invoice = Invoice.objects.all()
    return render(request, 'viewallinvoice.html', {'invoice': invoice})


def EditInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    if request.method == 'POST':
        date = request.POST.get("date")
        to = request.POST.get("to")
        abn = request.POST.get("abn")
        site = request.POST.get("site")
        description = request.POST.getlist("description")
        quantity = request.POST.getlist("quantity")
        subtotal1 = request.POST.getlist("subtotal1")
        gst1 = request.POST.getlist("gst1")
        total1 = request.POST.getlist("total1")

        subtotal = request.POST.get("subtotal")
        gst = request.POST.get("gst")
        total = request.POST.get("total")

        company = Company.objects.get(id=invoice.quote.job.company.id)
        company.name = to
        company.builder_abn = abn
        company.save()

        job = Job.objects.get(id=invoice.quote.job.id)
        job.site = site
        job.save()

        invoice.description1 = description[0]
        invoice.quantity1 = quantity[0]
        invoice.subtotal1 = subtotal1[0]
        invoice.gst1 = gst1[0]
        invoice.total1 = total1[0]
        invoice.save()

        try:
            invoice.description2 = description[1]
            invoice.quantity2 = quantity[1]
            invoice.subtotal2 = subtotal1[1]
            invoice.gst2 = gst1[1]
            invoice.total2 = total1[1]
            invoice.save()
        except:
            invoice.description2 = None
            invoice.quantity2 = None
            invoice.subtotal2 = None
            invoice.gst2 = None
            invoice.total2 = None
            invoice.save()

        try:
            invoice.description3 = description[2]
            invoice.quantity3 = quantity[2]
            invoice.subtotal3 = subtotal1[2]
            invoice.gst3 = gst1[2]
            invoice.total3 = total1[2]
            invoice.save()
        except:
            invoice.description3 = None
            invoice.quantity3 = None
            invoice.subtotal3 = None
            invoice.gst3 = None
            invoice.total3 = None
            invoice.save()

        today = datetime.date.today()
        invoice.date = today
        invoice.subtotal = subtotal
        invoice.gst = gst
        invoice.total = total
        invoice.save()
        return redirect('invoice:final_invoice', invoice.id)

    return render(request, 'jquery.html', {'invoice': invoice})


def FinalInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    return render(request, 'finalinvoice.html', {'invoice': invoice})