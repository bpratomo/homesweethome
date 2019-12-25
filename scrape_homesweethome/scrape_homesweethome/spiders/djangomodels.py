from scrapy.contrib.djangoitem import DjangoItem


class HomeItem(DjangoItem):
    django_model = Home

class ScreenshotItem(DjangoItem):
    django_model = Screenshot
    
class DistanceItem(DjangoItem):
    django_model = Distance
    

