from django.contrib import admin
from .models import information
from .models import hospital
from .models import dept
from .models import doctor1
from .models import news



# Register your models here.



admin.site.register(hospital)
admin.site.register(information)
admin.site.register(dept)
admin.site.register(doctor1)
admin.site.register(news)

