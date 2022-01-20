from django.http import HttpResponse
from django.shortcuts import render


def crm_main(request):
    template = 'crm/crm_main.html'
    return render(request, template)
