from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InsonlarAPIView.as_view()),
    path('insonlar/', insonlar, name='hammasi'),
]
