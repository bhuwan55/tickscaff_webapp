from django.shortcuts import render, redirect
from .models import	Gear, Ordergear, Job, Returnedgear


# Create your views here.


def index(request):
	return render(request, 'main/index.html',{})


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

	else:
		return render(request, 'gear/addgear.html', {})

	return render(request, 'gear/addgear.html',{})


def ViewGear(request):
	gear = Gear.objects.all()
	return render(request,'gear/viewgear.html',{'gear':gear,})


def AddJobs(request):
	gear = Gear.objects.all()
	if request.method == "POST":
		gear1 = request.POST.getlist('name')
		size = request.POST.getlist('size')
		used_quantity = request.POST.getlist('used_quantity')

		job = Job.objects.create(date = request.POST.get("date"))

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
		job.company_name = request.POST.get("company_name")
		job.save()
		return redirect('view_jobs')

	else:
		return render(request, 'jobs/addjobs.html', {'gear':gear})

	return render(request, 'jobs/addjobs.html',{'gear':gear})


def ViewJobs(request):
	jobs = Job.objects.all()
	if request.method == "POST":
		id = request.POST.get("job_id")
		job = Job.objects.get(id=id)

		status = request.POST.get("status")
		if status == "active":
			return redirect('view_jobs')
			pass
		else:
			job.status = status
			job.save()
			return redirect('return_jobs', id=id)

	return render(request,'jobs/viewjobs.html', {'jobs':jobs})


def AddReturned(request,id):
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
		return redirect('view_jobs')

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
				return render(request, 'return/viewreturn.html', {'job': job})
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