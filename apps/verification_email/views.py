from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.serializers import ValidationError

from .models import VerificationEmail
from .serializers import VerificationEmailSerializer, ConfirmEmailSerializer


class VerificationEmailModelViewSet(ModelViewSet):
    queryset = VerificationEmail.objects.all()
    serializer_class = VerificationEmailSerializer
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        serializer = VerificationEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Code sent successfully!'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors)


class ConfirmEmailModelViewSet(ModelViewSet):
    queryset = VerificationEmail.objects.all()
    serializer_class = ConfirmEmailSerializer
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        serializer = ConfirmEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # print(serializer)
            email = serializer.data.get('email')
            code = serializer.data.get('code')
            print(email, code)
            obj = VerificationEmail.objects.filter(email=email, code=code).exists()
            print(obj)
            return Response({'message': 'Code sent successfully!'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors)

