from .models import Medicine
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
from django.http import HttpResponse
from django.core import serializers

@api_view(['GET'])
def MedicineView(request):
    data = Medicine.objects.all()
    res = serializers.serialize('json',data)

    return HttpResponse(res, content_type='application/json') 