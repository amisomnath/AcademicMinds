from django.contrib import admin
from school_management_system_api import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Subject)
admin.site.register(models.Teacher)
admin.site.register(models.StudentSubjectMapping)
