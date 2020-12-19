from django.urls import path
from .api.v1.views import LinkListAPI, LinkDetailAPI

urlpatterns = [
    path('link/<str:_uuid>', LinkDetailAPI.as_view(), name="link_detail"),
    path('link/', LinkListAPI.as_view(), name="link_list")
]