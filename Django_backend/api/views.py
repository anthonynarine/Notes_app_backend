from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import NoteSerializer
from api.models import Note


@api_view( [ "GET", "POST" ])

def notes_list(request):
    if request.method == "GET":
        notes = Note.objects.all()
    
        title = request.GET.get("title", None)
        if title is not None:
            notes = notes.filter(name__icontsins=title)  #this django filter is explained below.  
        
        notes_serializer = NoteSerializer(notes, many=True)
        return Response(notes_serializer.data)
        # "SAFE=FALSE" FOR OBJECTS SERIALIZATION
    elif request.method == "POST":
        notes_data = JSONParser().parse(request)
        notes_serializer = NoteSerializer(data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return Response(notes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(notes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view( [ "GET", "PUT", "DELETE"])
def notes_detail(request, pk):    
    notes = get_object_or_404(Note, pk=pk)        
    if request.method == "GET":
        notes_serializer = NoteSerializer(notes);
        return Response(notes_serializer.data)        
    elif request.method == "PUT":
        notes_data = JSONParser().parse(request)
        notes_serializer = NoteSerializer(notes, data=notes_data);
        notes_serializer.is_valid(raise_exception=True) 
        notes_serializer.save()
        return Response (notes_serializer.data)      
    elif request.method == "DELETE":
        notes.delete()

        return Response ({'message': "Note was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    
    
    
    # LINE 17-19 EXPLAINED
    # Django filter allows users to filter down a queryset based on a model's fields.
    # The "icontains" checks if either the title of the description field contains the value of the 
    # search_terms.
