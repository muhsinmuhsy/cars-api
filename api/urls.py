from django.urls import path
from api.views import *

urlpatterns = [
    path('car/list', car_list, name='category-list'),

]