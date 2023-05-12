# from task.models import User
from task.serializers import LoginSerializer
from rest_framework import generics
from rest_framework.response  import Response
from django.contrib.auth import authenticate  
from rest_framework_simplejwt.tokens import RefreshToken


class LoginApiView(generics.GenericAPIView):
	serializer_class = LoginSerializer
	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= authenticate(request, username=serializer.data["username"], password=serializer.data["password"])
		if user is not None:
			refresh = RefreshToken.for_user(user)
			return Response(
				{"refresh":str(refresh),
				"access": str(refresh.access_token)
     }
			)
		else:
			return Response(
				{"Error","Invalid password and username"}
			)

# class SignUpApiView(generics.GenericAPIView):
# 	serializer_class = SignUpSerializer
# 	def post(self, request):
# 		serializer = self.get_serializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		user= authenticate(request, firstname=serializer.data["firstname"], secondname=serializer.data["secondname"],
# 		     email = serializer.data["email"],phonenumber=serializer.data["phonenumber"],
# 			 password=serializer.data["password"],confirmpassword=serializer.data["confirmpassword"])
# 		if user is not None:
# 			refresh = RefreshToken.for_user(user)
# 			return Response(
# 				{"refresh":str(refresh),
# 				"access": str(refresh.access_token)
#      }
# 			)
# 		else:
# 			return Response(
# 				{"Error","Invalid Details"}
# 			)

                              