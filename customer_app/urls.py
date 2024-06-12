from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_customer, name='upload_customer'),
    path('graph/<int:customer_id>/', views.customer_graph, name='customer_graph'),
]
