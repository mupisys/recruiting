from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def homePageView(request):
    return render(request, 'landpage.html')