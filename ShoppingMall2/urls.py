
from django.contrib import admin
from django.urls import path, include
from ShoppingMall2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('User.urls.user_urls')),
    path('items/', include('Item.urls.item_urls')),
    path('categories/', include('Item.urls.category_urls')),
    path('tags/', include('Item.urls.tags_urls')),
    path('me/', include('User.urls.me_urls')),
    path('media/uploads/item_images/<str:file_name>', views.image_view),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('histories/', include('Item.urls.history_urls')),
    path('', views.root_view),
]