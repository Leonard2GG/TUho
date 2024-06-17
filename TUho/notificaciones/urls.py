from django.urls import path
from notificaciones import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',(views.Bandeja), name="Bandeja"),
]