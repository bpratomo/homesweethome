from scrapy_djangoitem import DjangoItem
from browse.models import Home, Screenshot, Distance



class HomeItem(DjangoItem):
    django_model = Home

class ScreenshotItem(DjangoItem):
    django_model = Screenshot
    
class DistanceItem(DjangoItem):
    django_model = Distance
    

