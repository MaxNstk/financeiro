from api.serializers.category_serializer import CategorySerializer
from api.v1.viewsets.login_required_viewset import LoginRequiredModelViewSet
from finances.models import Category


class CategoryViewSet(LoginRequiredModelViewSet):
     serializer_class = CategorySerializer
     queryset = Category.objects.all()

     def get_queryset(self):
         return Category.objects.filter(user=self.request.user)
