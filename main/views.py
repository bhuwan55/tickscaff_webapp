from django.shortcuts import render, redirect, reverse
from .models import	Gear, Ordergear, Job, Returnedgear
from django.contrib.auth import authenticate, login as auth_login
from django.http import  HttpResponseRedirect
from company.models import Company


# Create your views here.


def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None:
			print("hello")
			context = {
				'message': "Incorrect Username or Password. Please Log in again",
			}
			return render(request,'registration/login.html',context)
			pass
		auth_login(request, user)
		return HttpResponseRedirect(reverse('main:index_page'))
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('main:index_page'))
	return render(request,'registration/login.html',{})


def index(request):
	gear_count = Gear.objects.all().count()
	job_count = Job.objects.all().count()
	company_count = Company.objects.all().count()
	active_job_count = Job.objects.filter(status="active").count()
	latest_gear = Gear.objects.latest('date')
	latest_job = Job.objects.latest('date')

	context={
		'gear_count': gear_count,
		'job_count': job_count,
		'company_count':company_count,
		'active_job_count': active_job_count,
		'latest_gear': latest_gear,
		'latest_job': latest_job
	}
	return render(request, 'main/index.html',context)


 # --------------------------------------CRUD of Gear-------------------------------------------------------
def AddGear(request):
	if request.method == "POST":
		name = request.POST.get("name")
		size = request.POST.get("size")
		avail_quantity = request.POST.get("avail_quantity")
		date = request.POST.get("date")
		unit_price = request.POST.get("unit_price")
		try:
			image = request.FILES['image']
		except:
			image = request.POST.get("image")

		gear = Gear.objects.create(name=name,size=size,avail_quantity=avail_quantity,image=image,date=date,unit_price=unit_price)
		gear.save()
		return redirect('view_gear')

	return render(request, 'gear/addgear.html',{})



def EditGear(request, id):
	gear = Gear.objects.get(id=id)
	if request.method == "POST":
		name = request.POST.get("name")
		size = request.POST.get("size")
		avail_quantity = request.POST.get("avail_quantity")
		date = request.POST.get("date")
		unit_price = request.POST.get("unit_price")
		try:
			image = request.FILES['image']
		except:
			image = request.POST.get("image")

		gear.name = name
		gear.size = size
		gear.avail_quantity = avail_quantity
		gear.date = date
		gear.unit_price = unit_price
		gear.image = image
		gear.save()

	return render(request,'gear/editgear.html', {'gear': gear})


def DeleteGear(request, id):
	gear = Gear.objects.get(id=id)
	gear.delete()
	return redirect('main:view_gear')


def ViewGear(request):
	gear = Gear.objects.all()
	return render(request,'gear/viewgear.html',{'gear':gear,})



# --------------------------------------CRUD of JOb-------------------------------------------------------
def AddJobs(request):
	gear = Gear.objects.all()
	company = Company.objects.all()
	if request.method == "POST":
		gear1 = request.POST.getlist('name')
		size = request.POST.getlist('size')
		used_quantity = request.POST.getlist('used_quantity')
		company_id = request.POST.get('company')
		company = Company.objects.get(id=company_id)

		job = Job.objects.create(date = request.POST.get("date"),company=company)

		i = 0
		total_price = 0
		total_quantity = 0
		for gear1 in gear1:
			id, name = gear1.split(',')
			try:
				ordered_gear = Gear.objects.get(name=name,size=size[i])
			except Gear.DoesNotExist:
				message = " Size doesnot exists for selected Gear "
				job.delete()
				return render(request, 'jobs/addjobs.html', {'gear':gear,'message':message})
				pass

			ordered_gear.avail_quantity = ordered_gear.avail_quantity - int(used_quantity[i])
			ordered_gear.save()

			subtotal_price = float(used_quantity[i]) * float(ordered_gear.unit_price)

			total_quantity = total_quantity + int(used_quantity[i])
			total_price = total_price + subtotal_price

			orderobj = Ordergear.objects.create(gear=ordered_gear,used_quantity=used_quantity[i],subtotal_price=subtotal_price)
			orderobj.save()
			i = i+1
			job.order.add(orderobj)
		job.total_quantity = total_quantity
		job.total_price = total_price
		job.save()
		return redirect('main:view_jobs')

	return render(request, 'jobs/addjobs.html',{'gear':gear,'company':company})


def ViewJobs(request):
	jobs = Job.objects.all()
	if request.method == "POST":
		id = request.POST.get("job_id")
		job = Job.objects.get(id=id)

		status = request.POST.get("status")
		if status == "active":
			return redirect('main:view_jobs')
			pass
		else:
			job.status = status
			job.save()
			return redirect('main:return_jobs', id=id)

	return render(request,'jobs/viewjobs.html', {'jobs':jobs})


def EditJobs(request, id):
	job = Job.objects.get(id=id)
	company = Company.objects.all()
	gear = Gear.objects.all()

	if request.method == "POST":
		name = request.POST.getlist('name')
		size = request.POST.getlist('size')
		used_quantity = request.POST.getlist('used_quantity')
		return_id = request.POST.getlist('return_id')
		company_id = request.POST.get("company")

		company = Company.objects.get(id=company_id)
		job.company = company
		job.save()

# ------------------------------Remove gear--------------------------------------------------------
		for order in job.order.all():
			if str(order.id) not in return_id:
				orderobjs = Ordergear.objects.get(id=order.id)

				gear = Gear.objects.get(id=orderobjs.gear.id)
				gear.avail_quantity = gear.avail_quantity + orderobjs.used_quantity
				gear.save()

				job.order.remove(orderobjs)
				job.save()
				orderobjs.delete()

		i = 0
		total_price = 0
		total_quantity = 0
		for name in name:
			try:
				ordered_gear = Gear.objects.get(name=name,size=size[i])
			except Gear.DoesNotExist:
				message = "Gear provide gear information doesnot exists"
				return render(request, 'jobs/addjobs.html', {'message':message})
				pass

#------------------------------update existing-gear-values------------------------------------------------
			if int(return_id[i]) > 0:
				orderobj = Ordergear.objects.get(id=return_id[i])

				if int(used_quantity[i]) == orderobj.used_quantity:
					job.save()
					pass
				else:
					ordered_gear.avail_quantity = ordered_gear.avail_quantity + orderobj.used_quantity - \
												  int(used_quantity[i])
					ordered_gear.save()

					orderobj.used_quantity = used_quantity[i]
					orderobj.save()

				subtotal_price = float(used_quantity[i]) * float(ordered_gear.unit_price)

				total_quantity = total_quantity + int(used_quantity[i])
				total_price = total_price + subtotal_price

				orderobj.subtotal_price = subtotal_price
				orderobj.save()
# ------------------------------Create new-gear order------------------------------------------------
			else:
				ordered_gear.avail_quantity = ordered_gear.avail_quantity - int(used_quantity[i])
				ordered_gear.save()

				subtotal_price = float(used_quantity[i]) * float(ordered_gear.unit_price)

				total_quantity = total_quantity + int(used_quantity[i])
				total_price = total_price + subtotal_price

				orderobj = Ordergear.objects.create(gear=ordered_gear, used_quantity=used_quantity[i],
													subtotal_price=subtotal_price)
				orderobj.save()
				job.order.add(orderobj)
				job.save()
			i = i + 1

		job.total_quantity = total_quantity
		job.total_price = total_price
		job.save()

	return render(request, 'jobs/editjobs.html', {'job':job,'company':company,'gear':gear})


def DeleteJobs(request,id):
	job = Job.objects.get(id=id)
	for order in job.order.all:
		orderobj = Ordergear.objects.get(id=order.id)
		orderobj.delete()
	job.delete()
	return redirect('main:view_jobs')


# --------------------------------------CRUD of Returned order in JOb-------------------------------------------------------

def AddReturned(request, id):
	job = Job.objects.get(id=id)
	if request.method == "POST":
		name = request.POST.getlist('name')
		size = request.POST.getlist('size')
		returned_quantity = request.POST.getlist('returned_quantity')
		used_quantity = request.POST.getlist('used_quantity')

		i = 0
		fine_price = 0
		total_remain_quantity = 0

		for name in name:
			ordered_gear = Gear.objects.get(name=name , size=size[i])

			ordered_gear.avail_quantity = ordered_gear.avail_quantity + int(returned_quantity[i])
			ordered_gear.save()

			remain_quantity = int(used_quantity[i]) - int(returned_quantity[i])

			total_remain_quantity = total_remain_quantity + remain_quantity

			fine_price = fine_price + 0.1 * (remain_quantity) * float(ordered_gear.unit_price)

			returnobj = Returnedgear.objects.create(gear=ordered_gear, returned_quantity=returned_quantity[i],
												fine_price=fine_price,remain_quantity=remain_quantity)
			returnobj.save()
			i = i + 1
			job.returned.add(returnobj)
		job.total_remain_quantity = total_remain_quantity
		job.save()
		return redirect('main:view_jobs')

	return render(request, 'return/addreturn.html', {'job':job})


def ViewReturned(request,id):
	job = Job.objects.get(id=id)
	if request.method == "POST":
		name = request.POST.getlist('name')
		size = request.POST.getlist('size')
		returned_quantity = request.POST.getlist('returned_quantity')
		return_id = request.POST.getlist('return_id')

		i = 0
		total_remain_quantity = 0
		fine_price = 0
		for name in name:
			ordered_gear = Gear.objects.get(name=name, size=size[i])
			returnobj = Returnedgear.objects.get(id=return_id[i])
			used_quantity = returnobj.returned_quantity + returnobj.remain_quantity

			if int(returned_quantity[i]) == returnobj.returned_quantity:
				pass
			else:
				if int(returned_quantity[i]) < returnobj.returned_quantity:
					ordered_gear.avail_quantity = ordered_gear.avail_quantity - returnobj.returned_quantity + \
												  int(returned_quantity[i])
					ordered_gear.save()

					returnobj.returned_quantity = returned_quantity[i]
					returnobj.remain_quantity = used_quantity - int(returned_quantity[i])
					returnobj.save()
				else:
					ordered_gear.avail_quantity = ordered_gear.avail_quantity - returnobj.returned_quantity + \
												  int(returned_quantity[i])
					ordered_gear.save()

					returnobj.returned_quantity = returned_quantity[i]
					returnobj.remain_quantity = used_quantity - int(returned_quantity[i])
					returnobj.save()

			total_remain_quantity = total_remain_quantity + returnobj.remain_quantity

			fine_price = fine_price + 0.1 * (returnobj.remain_quantity) * float(ordered_gear.unit_price)
			i = i + 1

		job.total_remain_quantity = total_remain_quantity
		job.save()

	return render(request,'return/viewreturn.html', {'job':job})