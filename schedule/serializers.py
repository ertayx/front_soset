from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance.room.user.first_name)
        name = instance.room.user.first_name
        user_id = instance.room.user.id
        rep['info'] = {'name':name,'user_id':user_id}
        return rep