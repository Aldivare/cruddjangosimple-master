from multiprocessing import context
from django.shortcuts import render,redirect
from simplecrud.forms import CrudsimpleForm
from simplecrud.models import Crudsimple
from django.contrib import messages
from django.http import Http404

def tampildata(request):        
    return render(request,"index.html",{'tampilkandata':Crudsimple.objects.all()})

def inputdata(request):
    form = CrudsimpleForm()
    if request.method == "POST":
        form = CrudsimpleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task berhasil ditambahkan')
            return redirect('/') #Lihat Pada urls.py saat ingin men-redirect setelah aksi save.
    context = {'form':form}
    

    return render(request,'inputdata.html', context)

    

def hapusdata(request, nip):
    Crudsimple.objects.get(nip=nip).delete()
    return redirect('/')

def editdata(request, nip):
    try:
        data = Crudsimple.objects.get(pk=nip)
    except Crudsimple.DoesNotExist:
        raise Http404("Data tidak ditemukan")
    if request.method == 'POST':
        form = CrudsimpleForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CrudsimpleForm(instance=data)
    context = {
        'form': form
    }
    return render(request, 'editdata.html', context)

def lihatdata(request, nip):
    try:
        lihatdata = Crudsimple.objects.get(pk=nip)
        context = {
            'lihatdata': lihatdata
        }
    except Crudsimple.DoesNotExist:
        raise Http404("Task tidak ditemukan")
    return render(request, 'lihatdata.html', context)
