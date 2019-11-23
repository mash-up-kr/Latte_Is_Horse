from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BeverageListSerializers
from beverages.models import Beverage


class BeverageList(APIView):

    def get(self, request, format=None):
        beverages = Beverage.objects.all()
        serializer = BeverageListSerializers(beverages, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
