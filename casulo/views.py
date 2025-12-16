from django.shortcuts import render

def landpage(request):
    return render(request, "landpage.html")