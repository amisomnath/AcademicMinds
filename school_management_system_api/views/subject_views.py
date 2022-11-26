from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from school_management_system_api.models import Subject
from school_management_system_api.serializers.subject_serializers import SubjectSerializer


class SubjectViewSet(generics.CreateAPIView):
    """Handle view to create subject details"""

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SubjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
