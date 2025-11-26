
from django.urls import path
from advertisements.views import home_view 

urlpatterns = [
    path('', home_view),
]