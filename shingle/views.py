from django.shortcuts import render,redirect

# Create your views here.
from .statik_funck import create_shingles,hash_shingles
from .models import Textbase
from .forms import NameForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def CheckView(request):
    if request.method == 'POST':
        forms = NameForm(request.POST)
        if forms.is_valid():
            text_1=forms.cleaned_data['first_text']
            text_2=forms.cleaned_data['second_text']
            shtext_1=create_shingles(text_1,3)
            shtext_2 =create_shingles(text_2,3)
            hash_shingles_1 = hash_shingles(shtext_1)
            hash_shingles_2 = hash_shingles(shtext_2)
            intersection = set(hash_shingles_1).intersection(hash_shingles_2)
            natija = len(intersection) / len(shtext_1)

            # plagiat_koeffitsienti = len(hash_shingles_1) / len(hash_shingles_2)
            # print(plagiat_koeffitsienti)
        #print(forms)

        dic={
            'shtext_1':'Birinchi matin',
            'shtext_2': 'Ikkinchi matin',
            'natija':natija

        }
        context ={
            'val':dic
        }

        return redirect(context='asd',permanent=True)
    else:
        forms=NameForm()
        context = {
            'forms':forms
        }
        return render(request,'shingle/index.html',context)

def ResultView(request):

    return render(request,'xxx/index.html')

@api_view(['GET', 'POST'])
def XresultView(request):
    if request.method == 'POST':
        if not request.data['first_text']:
            return Response({"error": True,"first_text": "Matn birinchi kirtilmagan!"})
        if not request.data['second_text']:
            return Response({"error": True,"second_text": "Matn ikkinchi kirtilmagan!!"})
        if not request.data['number']:
            return Response({"error": True,"number": "Matnning bloklanish soni kirtilmagan!!"})
        block = int(request.data['number'])

        text_1=request.data['first_text']
        text_2=request.data['second_text']
        shtext_1 = create_shingles(text_1, block)

        shtext_2 = create_shingles(text_2, block)
        hash_shingles_1 = hash_shingles(shtext_1)

        hash_shingles_2 = hash_shingles(shtext_2)
        intersection = set(hash_shingles_1).intersection(hash_shingles_2)
        natija = (len(intersection) / len(shtext_1))
        data ={}
        data['natija']=natija
        return Response(data)
    elif request.method == 'GET':
        data = {}
        return Response({"error": "GET!"})
    else:
        return Response({"error": "result!"})
def DetailView(requests):
    obj=Textbase.objects.all()
    count=obj.count()
    context={'count':count}
    return render(requests,'shingle/chackbase.html',context)
@api_view(['GET', 'POST'])
def XSaveView(request):
    if request.method == 'POST':
        if not request.data['first_text']:
            return Response({"error": "false","first_text": "Matn kirtilmagan!"})

        text_1=request.data['first_text']
        try:
            obj=Textbase()
            obj.text_main=text_1
            obj.save()
            data ={
                'succes':True
            }
        except :
            data = {
                'error': True
            }
        return Response(data)
    elif request.method == 'GET':
        data = {}
        return Response({"error": "GET!"})
    else:
        return Response({"error": "result!"})
@api_view(['GET', 'POST'])
def XChackesView(request):
    if request.method == 'POST':
        if not request.data['first_text']:
            return Response({"error": True,"first_text": "Matn kirtilmagan!"})
        if not request.data['number']:
            return Response({"error": True,"number": "Matnning bloklanish soni kirtilmagan!!"})
        block = int(request.data['number'])
        text_1=request.data['first_text']
        objs=Textbase.objects.all()
        count=objs.count()
        summ=0
        for i in objs:
            shtext_1 = create_shingles(text_1, block)
            shtext_2 = create_shingles(i.text_main, block)
            hash_shingles_1 = hash_shingles(shtext_1)
            hash_shingles_2 = hash_shingles(shtext_2)
            intersection = set(hash_shingles_1).intersection(hash_shingles_2)
            natija = (len(intersection) / len(shtext_1))
            summ=summ+natija
        data={
            'natija':summ/count
        }
        return Response(data)
    elif request.method == 'GET':
        data = {}
        return Response({"error": "GET!"})
    else:
        return Response({"error": "result!"})