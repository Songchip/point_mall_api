from django.urls import path
from Item import views

urlpatterns = [
    path('<str:tag>/items/', views.TagsItems.as_view())
]