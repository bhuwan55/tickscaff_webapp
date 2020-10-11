from django.shortcuts import render, redirect
from .models import Invoice
from main.models import Job
from company.models import Company
from quote.models import Quote
from email.message import EmailMessage
from django.template.loader import get_template
from django.http import HttpResponse
import os
import smtplib
import pdfkit
import datetime
# Create your views here.


def CreateNewInvoice(request):
    company=Company.objects.all()
    if request.method== 'POST':
        date = request.POST.get("date")
        to = request.POST.get('to')
        print(to)
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

        try:
            current_company = Company.objects.get(name=to)
        except Company.DoesNotExist:
            current_company = Company.objects.create(name=to, builder_abn=abn)
            current_company.save()

        invoice = Invoice()
        invoice.to = to
        invoice.abn = abn
        invoice.site = site
        invoice.description1 = description[0]
        invoice.quantity1 = quantity[0]
        invoice.subtotal1 = subtotal1[0].replace(",", "")
        invoice.gst1 = gst1[0].replace(",", "")
        invoice.total1 = total1[0].replace(",", "")
        today = datetime.date.today()
        invoice.date_of_dismantle = today
        invoice.date = today
        invoice.subtotal = subtotal.replace(",", "")
        invoice.gst = gst.replace(",", "")
        invoice.total = total.replace(",", "")

        try:
            invoice.description2 = description[1]
            invoice.quantity2 = quantity[1]
            invoice.subtotal2 = subtotal1[1].replace(",", "")
            invoice.gst2 = gst1[1].replace(",", "")
            invoice.total2 = total1[1].replace(",", "")
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
            invoice.subtotal3 = subtotal1[2].replace(",", "")
            invoice.gst3 = gst1[2].replace(",", "")
            invoice.total3 = total1[2].replace(",", "")
            invoice.save()
        except:
            invoice.description3 = None
            invoice.quantity3 = None
            invoice.subtotal3 = None
            invoice.gst3 = None
            invoice.total3 = None
            invoice.save()

        invoice.save()
        return redirect('invoice:final_invoice', invoice.id)


    return render(request, 'createinvoice.html', {'company':company})


def CreateInvoice(request,id):
    quote = Quote.objects.get(id=id)
    total = quote.subtotal + quote.gst

    days = quote.hire_period * 7
    date_of_dismantle = quote.job.date_for_installation + datetime.timedelta(days=days)

    description1 = "Scaffold hire for " + str(quote.hire_period) + " weeks starting from, " + str(quote.job.date_for_installation) + " until " + str(date_of_dismantle) + "."
    quantity1 = str(quote.hire_period) + " weeks"

    invoice = Invoice.objects.create(subtotal1=quote.subtotal, gst1=quote.gst, total1=total\
                                     , date_of_dismantle=date_of_dismantle, subtotal=quote.subtotal\
                                     , gst=quote.gst, total=total, description1=description1\
                                    , quantity1=quantity1, site=quote.job.site,to=quote.job.company.name\
                                     , abn=quote.job.company.builder_abn)
    invoice.quote.add(quote)
    invoice.save()
    today = datetime.date.today()
    return redirect('invoice:final_invoice', invoice.id)


def ViewSingleInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    return render(request, 'finalinvoice.html', {'invoice': invoice, })


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

        # company = Company.objects.get(id=invoice.quote.job.company.id)
        # company.name = to
        # company.builder_abn = abn
        # company.save()

        # job = Job.objects.get(id=invoice.quote.job.id)
        # job.site = site
        # job.save()

        invoice.to = to
        invoice.abn = abn
        invoice.site = site
        invoice.description1 = description[0]
        invoice.quantity1 = quantity[0]
        invoice.subtotal1 = subtotal1[0].replace(",","")
        invoice.gst1 = gst1[0].replace(",","")
        invoice.total1 = total1[0].replace(",","")
        invoice.save()

        try:
            invoice.description2 = description[1]
            invoice.quantity2 = quantity[1]
            invoice.subtotal2 = subtotal1[1].replace(",","")
            invoice.gst2 = gst1[1].replace(",","")
            invoice.total2 = total1[1].replace(",","")
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
            invoice.subtotal3 = subtotal1[2].replace(",","")
            invoice.gst3 = gst1[2].replace(",","")
            invoice.total3 = total1[2].replace(",","")
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
        invoice.subtotal = subtotal.replace(",","")
        invoice.gst = gst.replace(",","")
        invoice.total = total.replace(",","")
        invoice.save()
        return redirect('invoice:final_invoice', invoice.id)

    return render(request, 'jquery.html', {'invoice': invoice})


def FinalInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    return render(request, 'finalinvoice.html', {'invoice': invoice})


def Sendmail(request, id):
    invoice = Invoice.objects.get(id=id)

    if request.method == 'POST':
        to = request.POST.get('to')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to
        msg.set_content(message)

        template = get_template('sendmailinvoice.html')
        html = template.render({ 'invoice':invoice})
        options = {
            'page-size': 'A4',
            'encoding': "UTF-8",
        }
        css = 'static/css/invoice.css'
        pdf = pdfkit.from_string(html, False, options, css=css)
        file_name = invoice.site  + " scaffold invoice.pdf"


        msg.add_attachment(pdf, maintype='application', subtype='octet-stream', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    return redirect('invoice:final_invoice', id=invoice.id)


def DeleteInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    invoice.delete()
    return redirect('invoice:view_all_invoice')


def ViewPdfInvoice(request, id):
    invoice = Invoice.objects.get(id=id)
    template = get_template('sendmailinvoice.html')
    html = template.render({'invoice': invoice})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    css = 'static/css/invoice.css'
    pdf = pdfkit.from_string(html, False, options, css=css)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    return response