from django.urls import path
from apps.Notificaciones import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',(views.Bandeja), name="Bandeja"),
]