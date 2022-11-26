from django.db import models

# Create your models here.


class Subject(models.Model):
    """Subject model for school management system"""

    class Meta:
        db_table = "subject"

    subject_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    textbook = models.CharField(max_length=255, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __int__(self):
        return self.id
