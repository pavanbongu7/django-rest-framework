from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HelloWorldSerializer


class HelloWorldView(APIView):
    def get(self, request, format=None):
        # serializer = HelloWorldSerializer()
        return Response({"data": "hello world new"})
