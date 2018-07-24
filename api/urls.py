from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('v1/books/', views.book.list, name='books'),
]
