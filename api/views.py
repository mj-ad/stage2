from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['GET'])
def get(request, pk, *args, **kwargs):
    """
    Get a paerticular person from database
    """
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request, *args, **kwargs):
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

@api_view(['POST'])
def update(request, pk, *args, **kwargs):
    """
    Update a persons details
    """
    person = get_object_or_404(Person, pk=pk)
    serialize = PersonSerializer(instance=person, serialize=request.data)
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

@api_view(['DELETE'])
def delete(request, pk, *args, **kwargs):
    """
    Delete a person from database
    """
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return Response(status=status.HTTP_202_ACCEPTED)