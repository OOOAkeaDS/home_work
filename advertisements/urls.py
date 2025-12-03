
from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.Ad, name='ads_list'),
    path("ads/<int:ad_id>/", views.get_ad_detail, name='ad_detail'),
    path('ads/add/', views.create_ad, name="ad_add"),
]