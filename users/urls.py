from django.urls import path
from .views import persons_view, person_detail_view

urlpatterns = [
    path('persons/', persons_view),           # GET (all), POST
    path('persons/<int:pk>/', person_detail_view),  # GET one, PUT, DELETE
]