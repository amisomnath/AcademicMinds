from django.db import models

# Create your models here.


class Student(models.Model):
    """Student model for school management system"""

    class Meta:
        db_table = "student"

    first_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    dob = models.DateField()
    address = models.TextField(null=True, blank=True, default=None)
    phone = models.CharField(max_length=255, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __int__(self):
        return self.id
