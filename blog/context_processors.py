from . models import *

def google_analytics_processor(request):
    analyticscode = AnalyticsCode.objects.all().first()            
    return {'analyticscode': analyticscode}