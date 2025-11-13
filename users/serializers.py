from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ["user", "date_payment", "payment_method"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
