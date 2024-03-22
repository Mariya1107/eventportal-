from django.urls import path
from eventportalapp.views import events


urlpatterns = [
    path('',events)
]
