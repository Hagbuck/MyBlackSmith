from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

import json

# def index(request):
#     return render(request, 'chess/index.html')

class ChessView(generic.TemplateView):
    template_name = "chess/index.html"

def move(request):
    data_to_dump = {'name' : 'chef'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, content_type='application/json')