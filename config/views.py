from django.shortcuts import render

def handler404(request):
    return render(request, 'error/404.html')

def handler500(request):
    return render(request, 'error/500.html')
