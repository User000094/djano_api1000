from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalDetails
from .serializers import PersonalDetailsSerializer


# 🔹 GET ALL + POST (CREATE)
@api_view(['GET', 'POST'])
def persons_view(request):

    # ✅ GET ALL
    if request.method == 'GET':
        persons = PersonalDetails.objects.all()
        serializer = PersonalDetailsSerializer(persons, many=True)
        return Response(serializer.data)

    # ✅ CREATE
    elif request.method == 'POST':
        serializer = PersonalDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 GET ONE + PUT + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def person_detail_view(request, pk):

    try:
        person = PersonalDetails.objects.get(id=pk)
    except PersonalDetails.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    # ✅ GET ONE
    if request.method == 'GET':
        serializer = PersonalDetailsSerializer(person)
        return Response(serializer.data)

    # ✅ UPDATE
    elif request.method == 'PUT':
        serializer = PersonalDetailsSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ DELETE
    elif request.method == 'DELETE':
        person.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)