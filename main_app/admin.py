from django.contrib import admin
from .models import Car , Tuneup , Mod
# Register your models here.
admin.site.register(Car)
# register the new Tuneup Model 
admin.site.register(Tuneup)
admin.site.register(Mod)
