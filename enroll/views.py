from django.shortcuts import render , HttpResponseRedirect

from.forms import StudentRegistration
from.models import User

# Create your views here.

# This Function Will add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm =fm.cleaned_data['name']
            em =fm.cleaned_data['email']
            pw =fm.cleaned_data['password']
            reg = User(name =nm, email =em ,password = pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm =StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/show.html',{'form':fm ,'stu':stud}) 

# This Function Will Update/Edit
def data_update (request,id):


   if request.method == 'GET':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':fm})

      
   if request.method =='POST':
        pi =User.objects.get(pk=id)
        fm =StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    
        return render(request,'enroll/updatestudent.html',{'form':fm})
        

# This Function Will Delete
def data_delete(request,id):
 if request.method == 'POST':
  pi= User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')



   
