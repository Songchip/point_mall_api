from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Item.serializers import UserItemSerializer
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.hashers import make_password


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print("111")
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class MyItemsView(GenericAPIView):
        permission_classes = [permissions.IsAuthenticated]
        serializer_class = UserItemSerializer

        def get(self, request):
            serializer = self.get_serializer(request.user.items.all(), many=True)
            return Response(serializer.data)





class UserViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def items(self, request,  *args, **kwargs):
        user = self.get_object()
        serializer = UserItemSerializer(user.items.all(), many=True)

        return Response(serializer.data)

    def perform_create(self,serializer):
        serializer.save(
            password = make_password(self.request.data['password'])
        )

    # /users/test/ 해야 불림
    @action(detail=False, methods=['POST'])
    def test(self, request, *args, **kwargs):
        print("test")

    @action(detail=True, methods=['POST'])
    def point_charge(self, request, *args, **kwargs):
        print(request.data)
        user_point = int(request.data['point'])
        print(user_point)

        user = request.user
        print(user.point)
        user.point += user_point
        user.save()

        serializer = UserSerializer(request.user)
        return Response(serializer.data)