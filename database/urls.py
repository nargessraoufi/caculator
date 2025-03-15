from django.urls import path
from .views import SaveCalculationView, HistoryView  # Viewها را وارد کنید

urlpatterns = [
    path('save-calculation/', SaveCalculationView.as_view(), name='save-calculation'),
    path('history/', HistoryView.as_view(), name='history'),
]