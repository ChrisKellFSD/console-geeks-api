from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Contact
        fields = ['owner', 'name', 'subject', 'message']