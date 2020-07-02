from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_reminder', views.add_reminder, name='add_reminder'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/updating/', views.updating, name='updating'),
    path('<int:id>/delete', views.delete, name='delete'),
]