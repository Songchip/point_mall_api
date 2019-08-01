from rest_framework.routers import DefaultRouter

from Item import views

router = DefaultRouter()
router.register('', views.ItemViewSet)

urlpatterns = router.urls
