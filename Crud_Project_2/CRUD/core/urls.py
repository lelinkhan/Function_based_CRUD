from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:id>/',views.edit_student, name='edit_student'),
    path('delete/<int:id>/',views.delete_student, name='delete_student'),
]