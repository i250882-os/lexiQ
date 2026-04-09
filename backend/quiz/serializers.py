from rest_framework import serializers

class GenerateQuizSerializer(serializers.Serializer):
    id = serializers.IntegerField()
