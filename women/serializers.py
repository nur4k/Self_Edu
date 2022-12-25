from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Women



class WomenSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"
