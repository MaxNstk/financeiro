from api.serializers.transaction_serializer import TransactionSerializer
from api.v1.viewsets.login_required_viewset import LoginRequiredModelViewSet
from finances.models import Transaction


class TransactionViewSet(LoginRequiredModelViewSet):
    Serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


