from django.urls import path
from vusi.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
]