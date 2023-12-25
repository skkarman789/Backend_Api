from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.serializers import MyModelSerializer
from backend.models import Data
from rest_framework import status


# API endpoint to post event 
@api_view(['POST'])
def addItem(request):
    serializer = MyModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Event received successfully', 'data_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# API endpoint to get all events posted 
@api_view(['GET'])
def getData(request):
    notes = Data.objects.all()
    serializer = MyModelSerializer(notes, many=True)
    return Response(serializer.data)