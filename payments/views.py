from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment

from payments.serializers import PaySerializer, PaymentModelSerializer


# Create your views here.

class PayAPIView(APIView):
    serializer_class = PaymentModelSerializer

    def get(self, request):
        try:
            payments = Payment.objects.all().order_by('-id')
            serializer = self.serializer_class(payments, many=True)
            return Response({
                'status': True,
                'message': 'Jibambe payments',
                'payments': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'We could not retrieve payment records'
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided.',
                    'detail': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'status': True,
                'message': 'Payment processed successfully'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'An error occurred while processing payment.'
            }, status=status.HTTP_400_BAD_REQUEST)
