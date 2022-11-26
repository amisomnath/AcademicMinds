from rest_framework import serializers
from school_management_system_api import models
from school_management_system_api.serializers.subject_serializers import SubjectSerializer
from school_management_system_api.serializers.student_serializers import StudentSerializer


class StudentSubjectMappingSerializer(serializers.ModelSerializer):
    """Serializes a student subject mapping object"""

    class Meta:
        model = models.StudentSubjectMapping
        fields = ('id', 'student', 'subject')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.student:
            response['student'] = StudentSerializer(instance.student).data

        if instance.subject:
            response['subject'] = SubjectSerializer(instance.subject).data

        return response
