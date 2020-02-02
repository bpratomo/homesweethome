from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/property_list', methods=['POST'])
def property_list_from_event_ajax(payload):
    content = request.json
    
    event_type = content['event_type']

    try:
        event_data = json.loads(content['event_data']) 
    except:
        return HttpResponse('')
        
    
    if event_data is None:
        return HttpResponse('')


    elif event_type == 'relayout':
        xvar = content['xvar']
        yvar = content['yvar']

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






    return render(request,'browse/home_gallery.html',object_list=object_list)