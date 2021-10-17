from django.urls import path
from .views import *
urlpatterns = [
    path('main_sections', get_all_main_sections_view),
    path('main_section/<int:pk>/sections', get_all_sections_view),
    path('section/<int:pk>/products', get_all_products_view),
]