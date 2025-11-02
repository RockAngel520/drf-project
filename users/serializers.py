from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
