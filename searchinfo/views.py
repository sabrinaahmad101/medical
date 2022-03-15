from django.shortcuts import render, redirect
from .models import information
from .models import hospital
from .models import booking1
from .models import doctor1
from .models import dept
from .models import news


# Create your views here.




def booking(request):
    if request.method == 'POST':
        hospitsl_name = request.POST['hospitsl_name']
        booking_type = request.POST['booking_type']
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        payment_type = request.POST['payment_type']
        card_no = request.POST['card_no']
        bkash_no = request.POST['bkash_no']
        address = request.POST['address']
        ref = booking1(hospitsl_name=hospitsl_name, booking_type=booking_type,  name=name, email=email, address=address, bkash_no= bkash_no, card_no=card_no, payment_type=payment_type, phone_no=phone_no )
        ref.save()
        return redirect('/')

    else:

        return render(request, "booking_js.html")




    

def check_seat1(request):

    infos = information.objects.all()
    return render(request, "seat_check.html",{'infos' : infos})




def confirmation(request):
    return render(request, "confirmation.html")



def search(request):
  
    dests = hospital.objects.all()
    return render(request, "searching.html",{'dests' : dests})




def oxygensup(request):
    return render(request, "oxygen supply.html")




def oxlist(request):
    return render(request, "oxy_list.html")



def doc(request):
    doctors = doctor1.objects.all()

    return render(request, "consult_data1.html",{'doctors' : doctors})



def docpro(request):

    return render(request, "doc_pro.html")




def doc_pro(request, pk_test):
   doctors = doctor1.objects.get(id=pk_test)
   infos = doctor1.objects.all()
   context = {'doctors' : doctors, 'infos': infos}
   return render(request, 'doc_pro.html', context)





def home(request):
    infos = dept.objects.all()
    newsup= news.objects.all()
    context = {'newsup' : newsup, 'infos': infos}
    return render(request, 'home.html', context)




def consult_data1(request, pk_test):
   depts = dept.objects.all()
   doctors = doctor1.objects.filter(dept_id=pk_test)
   # doc_id=doctors.id
   infos = doctor1.objects.all()
   context = {'doctors' : doctors, 'infos': infos, 'depts': depts}
   return render(request, 'consult_data1.html', context)








   
    




