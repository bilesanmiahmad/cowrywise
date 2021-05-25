from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import DataModel

# Create your views here.

class DataModelViewSet(viewsets.ViewSet):

    def list(self, request):
        data_object = DataModel.objects.create()
        data_list = DataModel.objects.all()
        data_dict = {str(obj.created): obj.uuid for obj in data_list}
        return Response(data_dict)
