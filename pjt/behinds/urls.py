from django.urls import path
from . import views
app_name = "behinds"
urlpatterns = [
     path('', views.index, name="index"),
     path('create/', views.create, name="create"),
     path('<int:behind_pk>/detail', views.detail, name="detail"),
     path('<int:behind_pk>/delete', views.delete, name="delete"),
     path('<int:behind_pk>/update', views.update, name="update"),
]
