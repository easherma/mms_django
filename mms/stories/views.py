from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("check out this siick index")

def prompts(request, prompt_id):
    return HttpResponse("Looking at story %s" % prompt_id)

def results(request, prompt_id):
    reponse = "Looking at %s."
    return HttpResponse(response % prompt_id)

def count(request, prompt_id):
    return HttpResponse("You're submitting to %s" % prompt_id)
