from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class LoginRequiredModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)
    http_method_names = ['get','post','put']