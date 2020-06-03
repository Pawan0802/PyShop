from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Product Index Page')


def new(request):
    return HttpResponse('New Product')





