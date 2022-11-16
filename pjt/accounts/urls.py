from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('password/', views.password, name="password"),
    path('<int:user_pk>/profile/', views.profile, name="profile"),
    path('<int:user_pk>/update/', views.update, name="update"),
    path('<int:user_pk>/delete/', views.delete, name="delete"),
    path('<int:user_pk>/follow/', views.follow, name="follow"),
]
