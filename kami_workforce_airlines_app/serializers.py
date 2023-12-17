from django.core import serializers
from .models import Airplane

serializers.serialize('json', Airplane.objects.all())