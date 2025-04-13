from rest_framework import serializers

from .models import Vacancy, Company


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):

        instance = Company.objects.create(
            name=validated_data.get("name")
        )
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer2()

    class Meta:
        model = Vacancy
        fields = "__all__"
