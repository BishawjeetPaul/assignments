from rest_framework import serializers
from test_app.models import Test

class TestSerializer(serializers.Serializer):
	test_data = serializers.CharField()

	def create(self, validated_data):
		return Test.objects.create(**validated_data)