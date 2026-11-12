from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:booking_id>/', views.ticket_view, name='ticket_view'), # Naya E-Ticket route
]