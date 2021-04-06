from django.contrib import admin
from .models import Country
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Country)
class ViewAdmin(ImportExportModelAdmin):
     #exclude = ('id','Rank')
     pass