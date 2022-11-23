from django.urls import path
from .views import *

urlpatterns = [
    path("",FunctionalitiesListView.as_view(),name='func_list'),
    path("detail/<int:pk>",FunctionalityDetailView.as_view(),name='func_detail'),
]
