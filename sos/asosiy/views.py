from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

class InsonlarAPIView(APIView):
    def post(self, request):
        inson = request.data
        serializer = InsonSerializer(data=inson)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def insonlar(request):
        data = {"insonlar": Inson.objects.filter(faol=True)}
        return render(request, "home.html", data)

