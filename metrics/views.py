from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import MilkMetric
from .serializers import MilkMetricSerializer

class MilkMetricViewSet(viewsets.ModelViewSet):
    queryset = MilkMetric.objects.all().order_by('-timestamp')
    serializer_class = MilkMetricSerializer

def dashboard(request):
    latest_metrics = MilkMetric.objects.all().order_by('-timestamp')[:10]
    return render(request, 'metrics/dashboard.html', {'metrics': latest_metrics})

@csrf_exempt
@api_view(['POST'])
def esp32_data(request):
    if request.method == 'POST':
        serializer = MilkMetricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        return Response({'status': 'error', 'errors': serializer.errors})
