from django.contrib import admin

# Register your models here.
from AdminApp.models import CuisineDb,DishDb

admin.site.register(CuisineDb)
admin.site.register(DishDb)

