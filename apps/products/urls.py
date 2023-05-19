from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet, CategoryModelViewSet

router = DefaultRouter()


router.register('product', ProductModelViewSet)
router.register('category', CategoryModelViewSet)


urlpatterns = router.urls
