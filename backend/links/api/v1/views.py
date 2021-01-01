import rest_framework.generics as generics
from django.db import DataError
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
        days_to_delete = request.data.get('days', 60)

        data = {
            'initial_link': request.data['initial_link'],
            'truncated_link_uuid': request.data.get('truncated_link_uuid', None)
        }
        try:
            _link = Link.objects.create(initial_link=data['initial_link'],
                                        truncated_link_uuid=data['truncated_link_uuid'])
            _link.save()
            serializer = self.serializer_class(_link)

            print(serializer.data)
            delete_link.apply_async(args=[serializer.data['truncated_link_uuid']],
                                    eta=datetime.utcnow() + timedelta(days=days_to_delete))
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        except DataError:
            return Response({
                'error': 'link is too long'
            })
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    lookup_url_kwarg = 'truncated_link_uuid'

    def get(self, request, truncated_link_uuid):
        _queryset = Link.objects.get(truncated_link_uuid=truncated_link_uuid)
        serializer = self.serializer_class(_queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
