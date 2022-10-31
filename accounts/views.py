from os import stat
import requests
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getUser(request):
    try:
        users = request.user
        users_json = UserSerializer(users)
        data = {
            'data': users_json.data
        }
    except Exception as e:
        data = {
            'error': f'{e}'
        }
    return Response(data)


@api_view(['POST'])
@authentication_classes([])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
        req = {
            'username': username,
            'password': password
        }
        url = 'http://127.0.0.1:8000/auth/token/'
        res = requests.post(url, req)
        data = res.json()
    except Exception as e:
        data = {
            'error': f'{e}'
        }
    return Response(data)


@api_view(['POST'])
@authentication_classes([])
def register(request):
    try:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        username = request.data['username']
        password1 = request.data['password1']
        password2 = request.data['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                data = {
                    'error': "Bunday username mavjud"
                }
            elif User.objects.filter(email=email).exists():
                data = {
                    'error': "Bunday email mavjud"
                }
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=make_password(password1)
                )
                user.save()
                us = UserSerializer(request.data)
                data = {
                    'message': 'Muvaffaqiyatli ro`yhatdan o`tdingiz',
                    'data': us.data
                }
        else:
            data = {
                'error': "Parollar bir-biriga to'gri kelmadi"
            }
    except Exception as e:
        data = {
            'error': f'{e}'
        }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_user(request):
    user = request.user
    print(request.data.keys())
    if 'first_name' in request.data.keys():
        user.first_name = request.data['first_name']
    if 'last_name' in request.data.keys():
        user.last_name = request.data['last_name']
    if 'username' in request.data.keys():
        if not User.objects.filter(username=request.data['username']):
            user.username = request.data['username']
        else:
            data = {
                'error': 'Bunday username mavjud'
            }
            return Response(data, status=405)
    if 'email' in request.data.keys():
        if not User.objects.filter(email=request.data['email']):
            user.email = request.data['email']
        else:
            data = {
                'error': 'Bunday email mavjud'
            }
            return Response(data, status=405)
    user.save()
    data = {
        'data': UserSerializer(user).data
    }
    return Response(data)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication]) 
def delete(request):
    user = request.user
    user.delete()
    data = {
        'message': "O'chirildi"
    }
    return Response(data, status=204)