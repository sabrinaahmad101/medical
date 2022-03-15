from django.urls import path 
from . import views

urlpatterns = [
    path('check_seat1',views.check_seat1, name ='check_seat1'),
    path('booking2',views.booking, name ='booking'),
    path('confirmation',views.confirmation, name ='confirmation'),
    path('search',views.search, name ='search'),
    path('oxygensup',views.oxygensup, name ='oxygensup'),
    path('oxlist',views.oxlist, name ='oxlist'),
    path('doc',views.doc, name ='doc'),
    path('docpro',views.docpro, name='docpro'),
    path('doc_pro/<str:pk_test>/', views.doc_pro, name ='filter_doc'),
    path('consult_data1/<str:pk_test>/', views.consult_data1, name ='dep_doc'),
    path('home', views.home, name ='home')

    

]
