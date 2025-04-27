from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer

# GET /incidents -> Retrieve all incidents
@api_view(['GET'])
def get_all_incidents(request):
    incidents = Incident.objects.all()
    serializer = IncidentSerializer(incidents, many=True)
    return Response(serializer.data)

# POST /incidents -> Create a new incident
@api_view(['POST'])
def create_incident(request):
    serializer = IncidentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET /incidents/{id} -> Retrieve specific incident by id
@api_view(['GET'])
def get_incident_by_id(request, id):
    try:
        incident = Incident.objects.get(pk=id)
    except Incident.DoesNotExist:
        return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = IncidentSerializer(incident)
    return Response(serializer.data)

# DELETE /incidents/{id} -> Delete specific incident by id
@api_view(['DELETE'])
def delete_incident(request, id):
    try:
        incident = Incident.objects.get(pk=id)
    except Incident.DoesNotExist:
        return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
    
    incident.delete()
    return Response({'message': 'Incident deleted successfully.'}, status=status.HTTP_200_OK)
