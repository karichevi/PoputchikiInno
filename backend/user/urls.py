from django.urls import path

from . import views
from trips.models import CarTrip

app_name = "user"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
]
