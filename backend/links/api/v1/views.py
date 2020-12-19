import rest_framework.generics as generics
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from links.models import Link
from .serializers import LinkSerializer

from links.tasks import delete_link

from datetime import datetime, timedelta


class LinkListAPI(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = (AllowAny, )
    queryset = Link.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            delete_link.apply_async(args=[serializer.data['truncated_link_uuid']],
                                    eta=datetime.utcnow() + timedelta(days=30))
            return Response(serializer.data,
                            status=status.HTTP_200_OK)


class LinkDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    lookup_url_kwarg = '_uuid'
