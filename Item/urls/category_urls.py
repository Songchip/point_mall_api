from rest_framework.routers import DefaultRouter

from Item import views

router = DefaultRouter()
router.register('', views.CategoryViewSet)

urlpatterns = router.urls
