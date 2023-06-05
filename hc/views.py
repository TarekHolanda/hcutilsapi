from django.http import HttpResponse
from django.http import JsonResponse
from hc.models import Sprint
from hc.serializers import SprintSerializer


def index(request):
    return HttpResponse("Hello, HC!!!")


def sprint(request):
    data = Sprint.objects.all()
    serializer = SprintSerializer(data, many=True)
    return JsonResponse({"data": serializer.data})
