from rest_framework import serializers
from api.models import Mailing, Message, Client


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['mobile_operator']

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        if phone_number[0] != "7":
            raise serializers.ValidationError(
                "Phone number does not befit the 7XXXXXXXXXX pattern")
        if len(phone_number) != 11:
            raise serializers.ValidationError(
                "Phone number length should be 11")
        if not phone_number.isnumeric():
            raise serializers.ValidationError(
                "Phone number should be a numeric string")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.update(
            {"mobile_operator": validated_data['phone_number'][1:4]})
        return super().create(validated_data)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
