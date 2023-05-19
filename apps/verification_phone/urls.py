from django.urls import path
from .views import SendSMSView, VerifyPhoneNumberView


urlpatterns = [
    path('send_sms', SendSMSView.as_view()),
    path('verify', VerifyPhoneNumberView.as_view())
]
