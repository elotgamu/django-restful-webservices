from django.urls import path

from .views import toy_list, toy_details

urlpatterns = [
    path('', toy_list),
    path('<int:pk>', toy_details),
]
