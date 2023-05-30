from django.shortcuts import render
from .models import Storge_file
# Create your views here.

def IndexView(request):
    obj = Storge_file.objects.all()
    context={
        'files':obj
    }
    return render(request, 'storge_file/index.html',context)
