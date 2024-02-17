from django.shortcuts import render

# Create your views h-ere.
def index(request):
    return render(request, 'index.html', {})
