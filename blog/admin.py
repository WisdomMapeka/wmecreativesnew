from django.contrib import admin
from . models import Categories, Articles, Images, AnalyticsCode, Photos_collections

# Register your models here.
admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(AnalyticsCode)
admin.site.register(Photos_collections)
