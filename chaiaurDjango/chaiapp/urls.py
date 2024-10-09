
from django.urls import path
from . import views

# localhost:8000/chaiapp
# localhost:8000/chaiapp/order
urlpatterns = [
    path('', views.allChai, name='all_chai'),
    path('order/', views.allChai, name='all_home'),
]
