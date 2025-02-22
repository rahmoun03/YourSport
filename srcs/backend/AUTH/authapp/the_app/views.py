from django.shortcuts import render
from django.http import HttpResponse

def check(req):
    return HttpResponse("Working Successfuly...")
