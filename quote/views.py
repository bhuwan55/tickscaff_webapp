from django.shortcuts import render, redirect
from company.models import Company
from main.models import Job, Gear, Ordergear
from .models import Quote
from invoice.models import Invoice
from email.message import EmailMessage
from invoice.models import Invoice
from django.template.loader import get_template
import os
import smtplib
import pdfkit
import datetime
# Create your views here.


def CreateQuote(request):
    company = Company.objects.all()
    today = datetime.date.today()
    if request.method == 'POST':
        date = request.POST.get('date')
        company_name = request.POST.get('company')
        site = request.POST.get('site')
        builder_name = request.POST.get('builder_name')
        description1 = request.POST.get('description1')
        description2 = request.POST.get('description2')
        description3 = request.POST.get('description3')
        hire_period = request.POST.get('hire_period')
        new_scope = request.POST.get('new_scope')
        subtotal = request.POST.get('subtotal')
        gst = request.POST.get('gst')
        scope_end = request.POST.get('scope_end')

        try:
            current_company = Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            current_company = Company.objects.create(name=company_name, builder_name=builder_name)
            current_company.save()

        gears = Gear.objects.all()
        job = Job.objects.create(site=site, company=current_company)
        for gear in gears:
            ordergear = Ordergear.objects.create(gear=gear, used_quantity=0, subtotal_weight=0)
            job.order.add(ordergear)
        job.save()

        quote = Quote.objects.create(date=date, job=job, description1=description1\
               , description2=description2, description3=description3, hire_period=hire_period\
                , new_scope=new_scope, subtotal=subtotal, gst=gst, scope_end=scope_end)
        quote.save()
        return redirect('quote:view_single_quote', id=quote.id)

    return render(request, 'createquote.html', {'company':company, 'today':today,})


def ViewAllQuote(request):
    quotes = Quote.objects.all()
    return render(request, 'viewallquote.html', {'quotes':quotes})


def ViewSingleQuote(request, id):
    quote = Quote.objects.get(id=id)
    try:
        invoice = Invoice.objects.get(quote=quote)
    except Invoice.DoesNotExist:
        invoice = 1

    return render(request, 'viewsinglequote.html', {'quote': quote, 'invoice':invoice})


def EditQuote(request, id):
    company = Company.objects.all()
    quote = Quote.objects.get(id=id)
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        date = request.POST.get('date')
        company_name = request.POST.get('company')
        print(company_name)
        site = request.POST.get('site')
        builder_name = request.POST.get('builder_name')
        description1 = request.POST.get('description1')
        description2 = request.POST.get('description2')
        description3 = request.POST.get('description3')
        hire_period = request.POST.get('hire_period')
        new_scope = request.POST.get('new_scope')
        subtotal = request.POST.get('subtotal')
        gst = request.POST.get('gst')
        scope_end = request.POST.get('scope_end')

        try:
            current_company = Company.objects.get(name=company_name)
            # current_company.builder_name = builder_name
        except Company.DoesNotExist:
            current_company = Company.objects.create(name=company_name, builder_name=builder_name)
            current_company.save()

        job = Job.objects.get(id=job_id)
        job.site = site
        job.company = current_company
        job.save()

        quote.date = date
        quote.job = job
        quote.description1 = description1
        quote.description2 = description2
        quote.description3 = description3
        quote.hire_period = hire_period
        quote.new_scope = new_scope
        quote.subtotal = subtotal
        quote.gst = gst
        quote.scope_end = scope_end
        quote.save()
        return redirect('quote:view_single_quote', id=quote.id)

    return render(request, 'editquote.html', {'quote': quote, 'company':company})


def DeleteQuote(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    job = Job.objects.get(id=quote.job.id)

    return redirect('main:delete_jobs', id=job.id)

def Sendmail(request, id):
    quote = Quote.objects.get(id=id)
    try:
        invoice = Invoice.objects.get(quote=quote)
    except Invoice.DoesNotExist:
        invoice = 1

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

        template = get_template('mailquote.html')
        html = template.render({'quote': quote, 'invoice':invoice})
        options = {
            'page-size': 'A4',
            'encoding': "UTF-8",
        }
        css = 'static/css/quote.css'
        pdf = pdfkit.from_string(html, False, options, css=css)
        file_name = quote.job.site  + " scaffold invoice.pdf"


        msg.add_attachment(pdf, maintype='application', subtype='octet-stream', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    return redirect('quote:view_single_quote', id=quote.id)