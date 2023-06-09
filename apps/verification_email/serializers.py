from rest_framework import serializers

from .models import VerificationEmail
from .utils import generate_code, send_verification_code


class VerificationEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationEmail
        fields = ('email',)

    def create(self, validated_data):
        code = generate_code()
        email = validated_data['email']
        obj = VerificationEmail.objects.create(
            email=email,
            code=code
        )
        send_verification_code(email, code)
        return obj


class ConfirmEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationEmail
        fields = ('email', 'code')

