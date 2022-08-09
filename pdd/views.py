from django.shortcuts import render
from .models import Pdd
from jinja2 import Template
from django.http import JsonResponse


def question_number(request, num):

    return JsonResponse({"number": num})

def pdd(request):
    questions = Pdd.objects.all()

    return render(request, 'pdd/pdd.html', {'title': 'PDD', 'questions': questions})


def helper(request):
    return render(request, 'pdd/helper.html')


def main(request):
    return render(request, 'pdd/main.html')