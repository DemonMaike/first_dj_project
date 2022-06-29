from django.urls import include, path
from .views import exchange


app_name = 'moneys_converter'

urlpatterns = [
    path('', exchange),
]