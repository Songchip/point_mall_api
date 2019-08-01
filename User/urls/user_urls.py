from rest_framework.routers import DefaultRouter

from User import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = router.urls
