from django.shortcuts import render
from django.views.generic import ListView
from browse.models import Home


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'browse/index.html')

class property_list(ListView):
    paginate_by = 20
    model = Home



