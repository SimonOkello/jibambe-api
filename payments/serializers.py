from rest_framework import serializers

from payments.models import PAYMENT_CHOICES, Payment


class PaySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    payment_method = serializers.ChoiceField(choices=PAYMENT_CHOICES, default='CASH')
    amount = serializers.DecimalField(
        max_digits=16, decimal_places=2, default=0.0)


class PaymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','name', 'payment_method', 'amount']
