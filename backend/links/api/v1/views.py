import rest_framework.generics as generics
from rest_framework.permissions import AllowAny

from links.models import Link
from .serializers import LinkSerializer


class LinkListSerializer(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = AllowAny
    queryset = Link.objects.all()


class LinkDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = AllowAny
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    lookup_url_kwarg = 'uuid'
