from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django_opentracing import tracing
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, response, request
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken

import datetime

import logging



# Create your views here.
from empapp.models import EmployeeUserAuth, Address, Person
from empapp.serializers import LoginSerializer, CreateEmployeeSerializer, CreatePersonSerializer, \
    CreateAddressSerializer, UserSerializer, PersonSerializer
from empapp.utils.pagination import CustomPagination

logger = logging.getLogger(__name__)


@tracing.trace()
class Login(APIView):
    logger.warning('Login was accessed at ' + str(datetime.datetime.now()) + ' hours!')

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        response = []
        if serializer.is_valid():
            try:
                user = EmployeeUserAuth.objects.get(email=serializer.data['email'])
            except ObjectDoesNotExist:
                response = {'error': "no user found"}
            if user.password == serializer.data['password']:
                refresh = RefreshToken.for_user(user)
                response = {'access': str(refresh.access_token), 'refersh': str(refresh), "name": user.fullname}
        else:
            response = {"errors": serializer.error_messages}
        logger.info('Information incoming!')
        return Response(response)


@tracing.trace(view=True)
class CreateEmployee(APIView):
    logger.warning('create employee at ' + str(datetime.datetime.now()) + ' hours!')

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'fullname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'emp_position': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'emp_salary': openapi.Schema(type=openapi.TYPE_STRING, description='integer'),
            'emp_experience': openapi.Schema(type=openapi.TYPE_STRING, description='integer'),

        }
    ))
    def post(self, request, *args, **kwargs):

        try:
            user = request.data
            serializer = CreateEmployeeSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateAddress(APIView):
    logger.warning('create address at ' + str(datetime.datetime.now()) + ' hours!')

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'age': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'DOB': openapi.Schema(type=openapi.TYPE_STRING, description='integer'),
            'emp_id': openapi.Schema(type=openapi.TYPE_STRING, description='string'),

        }
    ))
    def post(self, request, *args, **kwargs):

        try:
            user = request.data
            serializer = CreateAddressSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CreatePerson(APIView):
    logger.warning('create person at ' + str(datetime.datetime.now()) + ' hours!')

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'emp_id': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'companyname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'phonenumber': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'zipcode': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'city': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'state': openapi.Schema(type=openapi.TYPE_STRING, description='integer'),
            }
    ))
    def post(self, request, *args, **kwargs):
        try:
            user = request.data
            serializer = CreatePersonSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAllemployee(ListAPIView):
    logger.warning('Get all employee at ' + str(datetime.datetime.now()) + ' hours!')
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        value = request.query_params
        users = EmployeeUserAuth.objects.filter()
        pagination = CustomPagination()
        page = pagination.paginate_queryset(queryset=users, request=request)
        result = pagination.get_paginated_response(page).data
        return (result)


class UpdateUser(GenericAPIView, UpdateModelMixin):
    logger.warning('update user at ' + str(datetime.datetime.now()) + ' hours!')

    queryset = EmployeeUserAuth.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return Response(status=200)


class UpdatePerson(APIView):
    def patch(self, request, *args, **kwargs):
        user = Person.objects.get(employee_id=request.query_params.get('id'))
        serializer = PersonSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DeleteEmployee(APIView):
    def delete(self, request, pk):
        user = EmployeeUserAuth.objects.filter(id=pk).get()
        user.delete()
        return Response(status=204)


class DeleteAddress(APIView):
    def delete(self, request, pk):
        user = Address.objects.filter(id=pk).get()
        user.delete()
        return Response(status=204)

