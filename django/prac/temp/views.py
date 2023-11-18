from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.template import loader
import os
from rest_framework.views import APIView
# Create your views here.


class HomeView(APIView):
    def get(self, request):
        template  = loader.get_template("home.html")
        return HttpResponse(template.render())