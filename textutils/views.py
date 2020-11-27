#I have created this views.py file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    djtext=request.POST.get('text','default')
    print(djtext)
    return HttpResponse("remove punc")

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    changecaps=request.POST.get('changecaps','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif changecaps=="on":
        analyzed=djtext.upper()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
