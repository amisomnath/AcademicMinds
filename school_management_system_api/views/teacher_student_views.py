from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from school_management_system_api.models import StudentSubjectMapping, Teacher
from school_management_system_api.serializers.student_subject_mapping_serializers import StudentSubjectMappingSerializer
from school_management_system_api.serializers.teacher_serializers import TeacherSerializer


class TeacherStudentMappingViewSet(generics.ListAPIView):
    """Handle view to fetch teacher student mapping details"""

    lookup_field = 'student_id'

    def list(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')
        subject_id = StudentSubjectMapping.objects.filter(student=student_id).values_list('subject', flat=True)
        teacher_name = Teacher.objects.filter(subject__in=subject_id)
        serializer = TeacherSerializer(teacher_name, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
