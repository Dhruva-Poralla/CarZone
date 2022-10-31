from django.urls import path
from . import views

urlpatterns = [
    path('enquery',views.enquery,name='enquery'),


]
