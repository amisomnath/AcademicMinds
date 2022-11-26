from django.db import models
from school_management_system_api.models import Subject, Student
# Create your models here.


class StudentSubjectMapping(models.Model):
    """Student and subject mapping model for school management system"""

    class Meta:
        db_table = "student_subject_mapping"

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='student_for_student_subject_mapping')
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='subject_for_student_subject_mapping')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __int__(self):
        return self.id
