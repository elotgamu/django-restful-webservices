from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Toy
from .serializers import ToyModelSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializers = ToyModelSerializer(toys, many=True)
        return Response(toys_serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # toy_data = JSONParser().parse(request)
        toy_serializer = ToyModelSerializer(data=request.data)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(
                toy_serializer.data,
                status=status.HTTP_201_CREATED)

        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toy_details(request, pk):

    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToyModelSerializer(toy)
        return Response(toy_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        toy_serializer = ToyModelSerializer(toy, data=request.data)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)

        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
