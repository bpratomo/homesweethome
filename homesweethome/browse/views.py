from django.shortcuts import render
from django.views.generic import ListView
from browse.models import Home
from .dashapp import app
from django.views.decorators.clickjacking import xframe_options_exempt
from django_pandas.io import read_frame
import pandas as pd 
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'browse/index.html')


class property_list(ListView):
    paginate_by = 20
    model = Home

def analytics(request):
    return render(request,'browse/home_analytics.html')


@csrf_exempt 
def property_list_from_event_ajax(request):

    event_type = request.POST.get('event_type')
    try:
        event_data = json.loads(request.POST.get('event_data'))  
    except:
        return HttpResponse('')
        
    
    if event_data is None:
        return HttpResponse('')


    elif event_type == 'relayout':
        xvar = request.POST.get('xvar')
        yvar = request.POST.get('yvar')

        event_data_keys = list(event_data)


        # return HttpResponse('')
         

        xmin = event_data[event_data_keys[0]]
        ymin = event_data[event_data_keys[2]]

        xmax = event_data[event_data_keys[1]]
        ymax = event_data[event_data_keys[3]]

        filter_dict = {
            xvar+'__gte':xmin,
            xvar+'__lte':xmax,
            yvar+'__gte':ymin,
            yvar+'__lte':ymax,
        }

        object_list  = Home.objects.filter(**filter_dict)
        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            properties = paginator.page(page)
        except PageNotAnInteger:
            properties = paginator.page(1)
        except EmptyPage:
            properties = paginator.page(paginator.num_pages)

        return render(request, 'browse/reusable/home_gallery.html', { 'object_list': properties })
        


    elif event_type == 'click':
        selected_object_id = event_data['points'][0]['customdata'][0]
        selected_object = Home.objects.filter(pk=selected_object_id)
        return render(request, 'browse/reusable/home_gallery.html', { 'object_list': selected_object })
        

    elif event_type == 'select':
        print('select event triggered')
        selected_object_id_list = []

        for point in event_data['points']:
            selected_object_id_list.append(point['customdata'][0])
        

        object_list  = Home.objects.filter(pk__in=selected_object_id_list)
        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            properties = paginator.page(page)
        except PageNotAnInteger:
            properties = paginator.page(1)
        except EmptyPage:
            properties = paginator.page(paginator.num_pages)
        
        return render(request, 'browse/reusable/home_gallery.html', { 'object_list': properties })

    
    else:
        return HttpResponse('no case triggered {}'.format(event_type))






    # return render(request,'browse/home_gallery.html',object_list=object_list)

    
