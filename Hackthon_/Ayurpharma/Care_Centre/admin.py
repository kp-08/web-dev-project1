from django.contrib import admin

# Register your models here.
from .models import MedicineData
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contact

class MedicineResource(resources.ModelResource):
    class Meta:
        model = MedicineData

class MedicineAdmin(ImportExportModelAdmin):
    resource_class = MedicineResource

admin.site.register(MedicineData, MedicineAdmin)      

admin.site.register(Contact)      


      