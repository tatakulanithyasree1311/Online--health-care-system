from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from patient.models import Doctor
from.serializer import DocSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
@api_view(['GET'])
def getdoctorapi(request):
    if request.method=='GET':
        doct=Doctor.objects.all()
        doct_objs=Docserializer(doct,many=True)
        return Response(doct_objs.data)