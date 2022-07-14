from django.http.response import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer, ChangePasswordSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                        context = {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user = user)
        data = ({
                'token': token.key, 'user_id': user.pk,
                'email': user.email, 'username': user.username,
                'address': user.profile.address, 'city': user.profile.city,
                'state': user.profile.state, 'zipcode': user.profile.zipcode,
                'first_name': user.first_name, 'last_name': user.last_name,
                'phone': user.profile.phone, 'staff': user.is_staff
            })
        return Response(data=data, status=status.HTTP_200_OK)


class RegisterUser(APIView):

    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data,
                        context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)


class UpdateUser(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        user = User.objects.get(id = pk)
        try:
            return user
        except User.DoesNotExist:
            raise Http404

    # Change Passwords
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        old_password = request.data.get('old_password')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        serializer = ChangePasswordSerializer(user, data=request.data)

        if serializer.is_valid():
            if password != password2:
                return Response({'password': 'Password does not match.'},
                                status=status.HTTP_400_BAD_REQUEST)

            if not user.check_password(old_password):
                return Response({'old_password': 'Wrong Password!'},
                                status=status.HTTP_400_BAD_REQUEST)

            user.set_password(password)
            user.save()
            return Response({'message': 'Password has been Changed'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deactivate User
    def post(self, request, pk, format=None):
        user = self.get_object(pk)
        password = request.data.get('password')

        if not user.check_password(password):
            return Response({'password': 'Wrong Password'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.is_active = False
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Update User Profile
class UpdateProfile(APIView):

    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        profile = Profile.objects.get(user = pk)
        try:
            return profile
        except Profile.DoesNotExist:
            return Http404

    def patch(self, request, pk, format=None):
        if request.user.is_authenticated:
            profile = self.get_object(pk)
            serializer = self.serializer_class(profile,
                            data=request.data,
                            context = {'request': request})

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


    