from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
def create(request, *args, **kwargs):
    """
    Create new person
    """
    serialize = PersonSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response({
            'data': serialize.data,
            'message': 'Successful'
            }, status=status.HTTP_201_CREATED)
    else:
        default = serialize.errors
        error = {}
        for field_name, field_errors in default.items():
            error[field_name] = field_errors[0]
        return Response({
            'message': 'Bad Request',
            'error': error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
def person(request, pk, *args, **kwargs):
    """
    Update a persons details ie get, update or delete
    """
    if request.method == 'PUT':
        person = get_object_or_404(Person, pk=pk)
        serialize = PersonSerializer(person, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({
                'data': serialize.data,
                'message': 'Successful'
                }, status=status.HTTP_201_CREATED)
        else:
            default = serialize.errors
            error = {}
            for field_name, field_errors in default.items():
                error[field_name] = field_errors[0]
            return Response({
                'message': 'Bad Request',
                'error': error}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)