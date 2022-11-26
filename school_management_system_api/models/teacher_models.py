from django.db import models
from school_management_system_api.models import Subject
# Create your models here.


class Teacher(models.Model):
    """Teacher model for school management system"""

    class Meta:
        db_table = "teacher"

    teacher_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='subject_for_teacher')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __int__(self):
        return self.id
