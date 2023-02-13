from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.



@api_view(['GET', 'POST'])
def productdetail(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            prod = productMainModel.objects.get(id=id)
            serializer = productMainModelSerializer(prod)
            return Response(serializer.data)

        prod = productMainModel.objects.all()
        serializer = productMainModelSerializer(prod, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = productMainModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET', 'POST'])
def getproducts(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            prod = getproduct.objects.get(id=id)
            serializer = getproductSerializer(prod)
            return Response(serializer.data)

        prod = getproduct.objects.all()
        serializer = getproductSerializer(prod, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = getproductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



@api_view(['GET', 'POST'])
def createuser(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            prod = userProfileModel.objects.get(id=id)
            serializer = userProfileModelSerializer(prod)
            return Response(serializer.data)

        prod = userProfileModel.objects.all()
        serializer = userProfileModelSerializer(prod, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = userProfileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
