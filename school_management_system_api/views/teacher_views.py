from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from school_management_system_api.models import Teacher
from school_management_system_api.serializers.teacher_serializers import TeacherSerializer


class TeacherViewSet(generics.CreateAPIView):
    """Handle view to create teacher details"""

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TeacherSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
