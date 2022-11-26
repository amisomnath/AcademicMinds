from rest_framework import serializers
from school_management_system_api import models
from school_management_system_api.serializers.subject_serializers import SubjectSerializer


class TeacherSerializer(serializers.ModelSerializer):
    """Serializes a teacher object"""

    class Meta:
        model = models.Teacher
        fields = ('id', 'teacher_name', 'subject')

    def to_representation(self, instance):
        response = super().to_representation(instance)

        if instance.subject:
            response['subject'] = SubjectSerializer(instance.subject).data

        return response
