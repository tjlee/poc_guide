from django.contrib import admin
from guidepocapp.models import Place, Guide, Region, GuideToPlace

admin.site.register(Place)
admin.site.register(Guide)
admin.site.register(Region)
admin.site.register(GuideToPlace)