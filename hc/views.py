from django.http import HttpResponse
from django.http import JsonResponse
from hc.models import Sprint
from hc.serializers import SprintSerializer


def index(request):
    return HttpResponse("Hello, HC!!!")


def sprints(request):
    data = Sprint.objects.all()
    serializer = SprintSerializer(data, many=True)
    return JsonResponse({"data": serializer.data})


def sprint(request):
    try:
        data = Sprint.objects.get(pk=1)
        serializer = SprintSerializer(data)
        return JsonResponse({"data": serializer.data})
    except Sprint.DoesNotExist:
        return HttpResponse(status=404)
