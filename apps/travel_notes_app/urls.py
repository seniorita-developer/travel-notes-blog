from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destinations', views.destinations, name='destinations'),
    path('destinations/<dest_id>', views.destination, name='destination'),
    path('new_destination', views.new_destination, name='new_destination'),
    path('new_entry/<dest_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry')

]