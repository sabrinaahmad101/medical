from django.contrib import admin
from .models import oxygensupply
from .models import record
from .models import doctor
from .models import user_profile
from .models import hos

# Register your models here.


admin.site.register(oxygensupply)
admin.site.register(record)
admin.site.register(user_profile)
admin.site.register(hos)
