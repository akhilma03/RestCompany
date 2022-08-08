from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serilaizer import UserSerializer,UserSerializerWithToken,ApplicationSerializer,UpdateSerializer
from .models import Application
from django.contrib.auth.hashers import make_password
from rest_framework import status

from sample import serilaizer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)

        serilaizer = UserSerializerWithToken(self.user).data
        for k,v in serilaizer.items():
            data[k] = v 

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
# def getRoutes(request):
#     return JsonResponse('hello', safe=False)


@api_view(['POST']) 
def registerUser(request):
    data = request.data
    try:
        user =User.objects.create(
            first_name= data['name'],
            username= data['email'],
            email = data['email'],
            password = make_password(data['password'])

        )
       
        serilaizer = UserSerializerWithToken(user,many=False)
        return Response(serilaizer.data)    
    except:
        message = {'detail':'User with this email already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user,many=False)   
    return Response(serializer.data)

 

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)   
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getApplication(request):
    application =  Application.objects.all()
    serializer = ApplicationSerializer(application,many=True) 
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getApplicationDetails(request,pk):
    application =  Application.objects.get(id=pk)
    serializer = ApplicationSerializer(application,many=False) 
    return Response(serializer.data)    


@api_view(['POST'])

def addApplication(request):
    data = request.data
    
    print(data)

    application =Application.objects.create(

        name= data['name'],
        Address= data['Address'],
        city = data['city'],
        state = data['state'],
        email = data['email'],
        phone = data['phone'],
        company_name = data['company_name'],
        compay_logo = data['compay_logo'],
        team_background = data['team_background'],
        about_companyProducts = data['about_companyProducts'],
        problems = data['problems'],
        uniqueSolution = data['uniqueSolution'],
        valueProposition = data['valueProposition'],
        revenue = data['revenue'],
        marketsize = data['marketsize'],
        marketplan = data['marketplan'],
        incubationtype = data['incubationtype'],
        detailProposal = data['detailProposal'],
       
    )
    
    serilaizer = ApplicationSerializer(application,many=False)
    print(serilaizer.data)
    return Response(serilaizer.data)    

@api_view(['POST'])
@permission_classes([IsAdminUser])
def StatusApplication(request,pk):
    application =  Application.objects.get(id=pk)
    serilaizer = UpdateSerializer(instance=application,data=request.data)

    if serilaizer.is_valid():
        serilaizer.save()

    return Response(serilaizer.data)  

@api_view(['DELETE'])
def DeleteApplication(request,pk):
    application =  Application.objects.get(id=pk)
    application.delete()
    
    return Response('item is deleted')