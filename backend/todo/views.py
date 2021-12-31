
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import TODO
from .serializers import TODOSerializer



class TODOViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for CRUD of TODO.
    """

    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("title", "user", "is_complete")
    search_fields = ("title")
    ordering_fields = ("is_complete", "created_at", "updated_at")

