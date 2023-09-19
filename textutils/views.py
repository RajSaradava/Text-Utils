# This file has been created by Raj

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # Check box values
    cb1 = request.POST.get('cb1', 'off')
    cb2 = request.POST.get('cb2', 'off')
    cb3 = request.POST.get('cb3', 'off')
    cb4 = request.POST.get('cb4', 'off')
    cb5 = request.POST.get('cb5', 'off')

    # Check which check box is checked
    if cb1 == "on":
            str = ""
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            for char in djtext:
                if char not in punctuations:
                    str = str + char
            parameters = {'purpose': 'Remove Punctuations', 'analyzed_text': str}
            djtext = str
            # analyze the text
            # return render(request,'analyze.html', parameters)
    if cb2 == "on":
            str = ""
            for char in djtext:
                    str = str + char.upper()
            parameters = {'purpose': 'CAPITALIZATION', 'analyzed_text': str}
            djtext = str
            # analyze the text
            # return render(request, 'analyze.html', parameters)
    if cb3 == "on":
            str = ""
            for char in djtext:
                if char != '\n'  and char != '\r':
                    str = str + char
            parameters = {'purpose': 'New Line Remover', 'analyzed_text': str}
            djtext = str
            # analyze the text
            # return render(request, 'analyze.html', parameters)
    if cb4 == "on":
            str = ""
            for ind, char in enumerate(djtext):
                if not(djtext[ind] == " " and djtext[ind+1] == " "):
                    str = str + char
            parameters = {'purpose': 'Extra Space Remover', 'analyzed_text': str}
            djtext = str
            # analyze the text
            # return render(request, 'analyze.html', parameters)
    if cb5 == "on":
            str = ""
            count = 0
            for char in djtext:
                if char != '\n':
                    count = count + 1
            parameters = {'purpose': 'Character Count', 'analyzed_text': count}
            # analyze the text

    if cb1 != "on" and cb2 != "on" and cb3 != "on" and cb4 != "on" and cb5 != "on":
            return HttpResponse("Please check at least one box")
    else :
        return render(request, 'analyze.html', parameters)
