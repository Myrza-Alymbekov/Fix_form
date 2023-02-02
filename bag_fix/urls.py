from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from project import settings
from .views import *

urlpatterns = [
    path('create/', ComplaintsCreateView.as_view(), name='complaints_create'),
    path('list/', ComplaintsListView.as_view(), name='complaints_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

