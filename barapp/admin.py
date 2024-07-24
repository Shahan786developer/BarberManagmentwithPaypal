from django.contrib import admin
from .models import *
admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(ShopReview)
