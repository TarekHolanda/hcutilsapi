from django.http import HttpResponse
from django.http import JsonResponse
from hc.models import Sprint
from hc.serializers import SprintSerializer
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, HC!!!")


def sprints(request):
    # Get all sprints sorted by index
    data = Sprint.objects.all().order_by("-index")
    serializer = SprintSerializer(data, many=True)

    return JsonResponse({
        "status": status.HTTP_200_OK,
        "data": serializer.data,
    })


def sprint(request):
    try:
        data = Sprint.objects.get(pk=1)
        serializer = SprintSerializer(data)
        return JsonResponse({"data": serializer.data})
    except Sprint.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
