from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import *
from .models import *
from rest_framework.response import Response


class CountryViews(viewsets.ViewSet):
  permission_classes=[permissions.AllowAny]






