from rest_framework import serializers
from hc.models import Sprint


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = "__all__"
