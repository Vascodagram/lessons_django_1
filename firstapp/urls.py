from django.contrib import admin
from django.urls import path
from firstapp.views import djangohello
urlpatterns = [
    path('', djangohello),
]