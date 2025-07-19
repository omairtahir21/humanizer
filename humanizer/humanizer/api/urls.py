from django.urls import path
from .views import humanize_view

urlpatterns = [
    path('humanize/', humanize_view),
]
