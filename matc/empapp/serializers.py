from rest_framework import serializers

from empapp.models import EmployeeUserAuth, Address, Person


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=2000, required=True)

    class Meta:
        fields = ['password','email']


class PersonSerializer(serializers.Serializer):
    age = serializers.IntegerField(default=0)
    DOB = serializers.IntegerField(default=0)


class CreateEmployeeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.CharField(max_length=100)

    class Meta:
        model = EmployeeUserAuth
        fields = ["id", "fullname", "username", "password", "emp_position", "emp_salary", "emp_experience", "email"]


class CreateAddressSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Address
        fields = "__all__"


class CreatePersonSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Person
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeeUserAuth
        fields = "__all__"

    def create(self, validated_data):
        user = EmployeeUserAuth.objects.create(**validated_data)
        user.is_active = True
        user.save()
        return user



