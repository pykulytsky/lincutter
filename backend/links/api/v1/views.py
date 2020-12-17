import rest_framework.generics as generics
from rest_framework.permissions import AllowAny

from links.models import Link
from .serializers import LinkSerializer


class LinkListSerilalizer(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
