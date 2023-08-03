from django.shortcuts import render

# Create your views here.


def static_image(request):
    return render(request,'static_image.html')
