from django.urls import path, include

from User import views

urlpatterns = [
    path('', views.MeView.as_view()),
    path('items/', views.MyItemsView.as_view())
]