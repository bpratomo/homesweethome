from django.shortcuts import render
from django.views.generic import ListView
from browse.models import Home
from .dashapp import app
from django.views.decorators.clickjacking import xframe_options_exempt
from django_pandas.io import read_frame
import pandas as pd 




# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'browse/index.html')


class property_list(ListView):
    paginate_by = 20
    model = Home

def testing_df(request):

    qs = Home.objects.all()

    df = read_frame(qs)

    all_columns = list(df.columns.values.tolist())
    all_columns.remove('id_from_website')
    all_columns.remove('id')
    print(all_columns)
    df = pd.melt(df,'id',all_columns)
    print(df)
    return HttpResponse(df)

