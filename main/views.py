# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import *
from django.contrib.auth import *
from .models import *
from .serializers import *


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class UniversityProgramsView2List(generics.ListAPIView):
    queryset = UniversityProgramsView2.objects.all()
    serializer_class = UniversityProgramsView2Serializer


class GeneralInformationView(generics.ListAPIView):
    queryset = GenelBilgilerLast2024.objects.all()
    serializer_class = GenaralInformationSerializer


class UniversitiesView(generics.ListAPIView):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer
