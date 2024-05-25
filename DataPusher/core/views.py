from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account,Destination
from .serializers import AccountSerializer,DestinationSerializer 
import requests

class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
class DestinationViewSet(viewsets.ModelViewSet):
    queryset=Destination.objects.all()
    serializer_class=DestinationSerializer

@api_view(['GET'])
def get_destinations(request,account_id):
    try:
        account=Account.objects.get(account_id=account_id)
    except Account.DoesNotExist:
        return Response({"error":"Account not found"},status=status.HTTP_404_NOT_FOUND)

    destinations=Destination.objects.filter(account=account)
    serializer=DestinationSerializer(destinations,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def incoming_data(request):
    app_secret_token=request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({"error":"Un Authenticate"},
        status=status.HTTP_401_UNAUTHORIZED)
    try:
        account=Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({"error":"Un Authenticate"},status=status.HTTP_401_UNAUTHORIZED)

    data=request.data
    if not isinstance(data,dict):
        return Response({"error":"Invalid Data"},status=status.HTTP_400_BAD_REQUEST)

    destinations=account.destinations.all()
    for destination in destinations:
        headers=destination.headers
        if destination.http_method=='GET':
            response=requests.request(destination.http_method,destination.url,headers=headers,json=data)
        elif destination.http_method in['POST','PUT']:
            response=requests.request(destination.http_method,destination.url,headers=headers,json=data)
    return Response({"message":"Data sent successfully"},status=status.HTTP_200_OK)       
    
# Create your views here.
