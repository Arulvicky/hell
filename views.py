import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

def one(request):
    hi=requests.get(' http://127.0.0.1:8000/').json()
    return JsonResponse(hi)
