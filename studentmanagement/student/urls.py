from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('show/', views.show, name='show'),
    path('show/delete/<int:id>', views.delete, name='delete'),
    path('show/update/<int:id>', views.update, name='update'),
    path('show/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

]