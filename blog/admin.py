from django.contrib import admin
from . models import Categories, Articles, Images, AnalyticsCode

# Register your models here.
admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(AnalyticsCode)
