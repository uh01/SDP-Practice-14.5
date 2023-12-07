from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="homepage"),
    path('about/', views.about, name ="aboutpage"),
    path('delete_M/<int:id_no>', views.detete_M, name ="deletedata"),
]