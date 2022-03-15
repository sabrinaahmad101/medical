from django.shortcuts import render, redirect
from . models import studentDetails, s_info



# Create your views here.





def index(request):
    if request.method == 'POST':
        idno =request.POST.get('idno')
        s_name = request.POST.get('s_name')
        

        marks = request.POST['marks']

        ref  =studentDetails(marks=marks, idno=idno, s_name= s_name)
        ref.save()

        return render(request,"travv.html",)
   
    else:
        return render(request,"travv.html",)
   
    


def index1(request):
    if request.method == 'POST':
        name_id = request.POST.get('name')
        name= studentDetails.objects.get(id=name_id)

        roll = request.POST.get('roll')

        ref  =s_info(name=name, roll=roll)
        ref.save()
        return render(request,"travv2.html",{'names' :studentDetails.objects.all(),'msg' : 'name added' })

       
    else:
        return render(request,"travv2.html",{'names' :studentDetails.objects.all() }) 



def book1(request):
    return render(request, "book1js.html")


def index3(request):
    return render(request, "travv2.html")