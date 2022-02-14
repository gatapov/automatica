from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import StoreSerializer, VisitSerializer
from .models import Store
from .permissions import HasPhone, IsEmployeeInStore


class StoreList(ListAPIView):
    serializer_class = StoreSerializer
    permission_classes = [HasPhone]

    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        return Store.objects.filter(employee__phone=phone)


class SetVisit(CreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = (HasPhone, IsEmployeeInStore)