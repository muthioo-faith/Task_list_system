from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


# class SignUpSerializer(serializers.Serializer):
#     firstname=serializers.CharField()
#     secondname=serializers.CharField()
#     email=serializers.EmailField()
#     phonenumber=serializers.CharField()
#     password=serializers.CharField()
#     confirmpassword=serializers.CharField()
