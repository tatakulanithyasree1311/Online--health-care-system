from rest_framework.serializers import ModelSerializer
from patient.models import Doctor
class DocSerializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'