from django.shortcuts import render
from django.views.generic import ListView
from browse.models import Home
from .dashapp import app
from django.views.decorators.clickjacking import xframe_options_exempt
from django_pandas.io import read_frame
import pandas as pd 
import json




# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'browse/index.html')


class property_list(ListView):
    paginate_by = 20
    model = Home

def analytics(request):
    return render(request,'browse/home_analytics.html')



# def property_list_from_event_ajax(request):
#     event_type = pass
#     object_list = pass  


#     return render(request,'browse/home_gallery.html',object_list=object_list)
    
