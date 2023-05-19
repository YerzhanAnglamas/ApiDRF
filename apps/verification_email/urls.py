from rest_framework.routers import DefaultRouter
from .views import VerificationEmailModelViewSet, ConfirmEmailModelViewSet

router = DefaultRouter()


router.register('send_code', VerificationEmailModelViewSet)
router.register('confirm_code', ConfirmEmailModelViewSet)


urlpatterns = router.urls
