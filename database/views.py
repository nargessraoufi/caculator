from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Calculation
from .serializers import CalculationSerializer

class SaveCalculationView(APIView):
    def post(self, request):
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryView(APIView):
    def get(self, request):
        calculations = Calculation.objects.all()
        serializer = CalculationSerializer(calculations, many=True)
        return Response(serializer.data)