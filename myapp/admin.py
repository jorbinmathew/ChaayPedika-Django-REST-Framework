from django.contrib import admin
from myapp.models import categorydb,productdb

# Register your models here.

admin.site.register(categorydb)
admin.site.register(productdb)