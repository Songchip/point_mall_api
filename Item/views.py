from .models import Item, UserItem, Category
from .serializers import ItemSerializer, UserItemSerializer, CategorySerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action






class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['POST'])
    def purchase(self, request, *args, **kwargs):

        count = int(request.data['count']);

        item = self.get_object()
        user = request.user
        if (item.price) * count > user.point:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
        user.point -= (item.price)*count
        user.save()
        try:
            user_item = UserItem.objects.get(user=user, item=item)
        except UserItem.DoesNotExist:
            user_item = UserItem(user=user, item=item)
        user_item.count += count
        user_item.save()

        serializer = UserItemSerializer(user.items.all(), many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True)
    def items(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = ItemSerializer(category.items.all(), many=True)

        return Response(serializer.data)