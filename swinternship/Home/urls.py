from django.urls import path
from .views import home
urlpatterns = [
    
    path('swinternship/',home,name='home'),
]