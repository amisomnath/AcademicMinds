from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from school_management_system_api.models import StudentSubjectMapping, Student, Subject
from school_management_system_api.serializers.student_subject_mapping_serializers import StudentSubjectMappingSerializer
from utils.constants.file import STUDENT_NOT_EXISTS, SUBJECT_NOT_EXISTS
from utils.exceptions.custom_exceptions import StudentNotExistsException, SubjectNotExistsException


class StudentSubjectMappingViewSet(generics.CreateAPIView):
    """Handle view to create student subject mapping details"""

    serializer_class = StudentSubjectMappingSerializer
    queryset = StudentSubjectMapping.objects.all()
    lookup_field = 'student_id', 'subject_id'

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
        except ObjectDoesNotExist:
            raise StudentNotExistsException(detail=STUDENT_NOT_EXISTS.format(student_id))
        subject_id = self.kwargs.get('subject_id')

        try:
            subject = Subject.objects.get(id=subject_id)
        except ObjectDoesNotExist:
            raise SubjectNotExistsException(detail=SUBJECT_NOT_EXISTS.format(subject_id))

        student_subject = StudentSubjectMapping.objects.update_or_create(student=student, subject=subject)
        obj = student_subject[0]

        serializer = StudentSubjectMappingSerializer(obj).data
        return Response(serializer, status=status.HTTP_201_CREATED)
