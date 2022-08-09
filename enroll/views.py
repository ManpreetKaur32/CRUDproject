from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegis
from .models import User


# Create your views here.
#This function add and view all data 
def add_show(request):
    if request.method == 'POST': 
        fm = StudentRegis(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegis()

            
    else:
        fm = StudentRegis()
    stud = User.objects.all()
    return render(request, 'enroll/addshow.html', {'form':fm, 'stu': stud})

#This function will update/edit
def update_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegis(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegis(instance=pi)
    return render(request, 'enroll/update.html', {'form': fm})
    # else:
    #     stud= User.objects.all()
    #     fm = StudentRegis()
    # return render(request, 'enroll/update.html', {'form':fm, 'stu':stud })
    # #this will show all data together

#This function will delete function
def delete_data(request, id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

