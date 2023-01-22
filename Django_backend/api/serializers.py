from rest_framework import serializers
from api.models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = "__all__"
        # fields = ( "id", "title", "body", "updated", "created" )
        
        
        
        # NOTE all fields can be serialized with "__all__" (python magic method)