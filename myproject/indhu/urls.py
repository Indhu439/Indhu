from django.urls import path
from.import views

urlpatterns=[
    path('data/',views.data_api)
]