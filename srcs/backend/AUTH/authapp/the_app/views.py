from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import creation_serializer
from rest_framework import status, response

def check(req):
    return HttpResponse("Working Successfuly...")

@api_view(["POST"])
def sign_up(req):
    print(f"Data {req.data}")
    serial = creation_serializer(data=req.data)
    if serial.is_valid():
        serial.save()
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(status=status.HTTP_400_BAD_REQUEST)