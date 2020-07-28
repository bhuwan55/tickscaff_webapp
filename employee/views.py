from django.shortcuts import render, redirect
from .models import Employee, Work
import datetime
from datetime import timedelta


# Create your views here.


def AddEmployee(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        employee = Employee(name=name,total_hours="0")
        employee.save()

    return render(request, 'addemployee.html', {})


def ViewEmployee(request):
    employee = Employee.objects.all().order_by("name")
    return render(request, 'viewemployee.html', {'employee':employee})


def DeleteEmployee(request,id):
    employee = Employee.objects.get(id=id)
    work = employee.work.all()
    for work in work:
        works = Work.objects.get(id=work.id)
        works.delete()
    employee.delete()
    return redirect('employee:view_employee')


def ViewSingleEmployee(request, id):
    employee = Employee.objects.get(id=id)
    today = datetime.date.today()
    year = today.year
    month= today.month

    todayss = datetime.date.today()
    start_week = todayss - datetime.timedelta(todayss.weekday()) - datetime.timedelta(days = 4)
    end_week = start_week + datetime.timedelta(6)
    works = employee.work.all().filter(date__range=[start_week, end_week])
    total_hours = employee.total_hours - employee.total_hours
    for work in works:
        total_hours = total_hours + work.hours

    if request.method == 'POST':
        date = request.POST.get("date")
        arrival_time = request.POST.get("arrival_time")
        signoff_time = request.POST.get("signoff_time")


        todays = request.POST.get("month")
        year = int(todays[0:4])
        month = int(todays[5:7])
        today = datetime.date(year, month, 1)


        work = Work.objects.create(date=date,arrival_time=arrival_time, signoff_time=signoff_time, hours="0")

        hours = work.get_time_diff()

        hr = int(hours[0:2])
        try:
            min = int(hours[9:11])
        except:
            min = 0

        work.hours = datetime.timedelta(hours=hr, minutes=min)

        employee.total_hours = employee.total_hours + work.hours
        work.save()

        employee.work.add(work)
        employee.save()
        return render(request, 'viewsingleemployee.html', {'employee': employee, 'works': works, 'today': today, })

    return render(request, 'viewsingleemployee.html', {'employee':employee, 'works':works,'today':today,'total_hours':total_hours,'start_week':start_week})


def DeleteWork(request,id):
    work = Work.objects.get(id=id)
    employee = work.employee_set.all()
    for employee in employee:
        if employee.total_hours > datetime.timedelta(hours=0, minutes=0):
            employee.total_hours = employee.total_hours - work.hours
    employee.save()
    work.delete()
    return redirect('employee:view_single_employee', id=employee.id)


def ChangeMonth(request, id):
    employee = Employee.objects.get(id=id)
    works = employee.work.all()
    today = datetime.date.today()

    todayss = datetime.date.today()
    start_week = todayss - datetime.timedelta(todayss.weekday()) - datetime.timedelta(days = 4)
    end_week = start_week + datetime.timedelta(6)
    works = employee.work.all().filter(date__range=[start_week, end_week])
    total_hours = employee.total_hours - employee.total_hours
    for work in works:
        total_hours = total_hours + work.hours

    if request.method == 'POST':
        x = request.POST.get("x")
        todays = request.POST.get("month")
        start_weeks = request.POST.get("start_week")
        year = int(start_weeks[0:4])
        month = int(start_weeks[5:7])
        day = int(start_weeks[8:10])
        start_week = datetime.date(year, month, day)
        if x == '-1':
            start_week = start_week - timedelta(days=7)
            end_week = start_week + datetime.timedelta(6)
        elif x == '1':
            start_week = start_week + timedelta(days=7)
            end_week = start_week + datetime.timedelta(6)
        works = employee.work.all().filter(date__range=[start_week, end_week])
        total_hours = total_hours - total_hours
        for work in works:
            total_hours = total_hours + work.hours
    return render(request, 'viewsingleemployee.html', {'employee': employee, 'works': works,'today':today,'start_week':start_week,'total_hours':total_hours})



def EditWork(request, id):
    work = Work.objects.get(id=id)
    employee = work.employee_set.all()
    if request.method == 'POST':
        id = request.POST.get("id")
        date = request.POST.get("date")
        arrival_time = request.POST.get("arrival_time")
        signoff_time = request.POST.get("signoff_time")


        work = Work.objects.get(id=int(id))
        work.date = date
        work.arrival_time = arrival_time
        work.signoff_time = signoff_time
        work.save()


        hours = work.get_time_diff()
        hr = int(hours[0:2])
        try:
            min = int(hours[9:11])
        except:
            min = 0
        for employee in employee:
            employee.total_hours = employee.total_hours - work.hours
            employee.save()

        work.hours = datetime.timedelta(hours=hr, minutes=min)
        work.save()

        employee.total_hours = employee.total_hours + work.hours
        employee.save()
        return redirect('employee:view_single_employee', id=employee.id)

    return render(request, 'editwork.html', {'work':work})