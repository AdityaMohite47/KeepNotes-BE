from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from notes.models import Note
from notes.serializers import NoteSerializer, RegisterSerializer
from notes.permissions import IsOwner


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], url_path='pin')
    def pin(self, request, pk=None):
        note = self.get_object() 
        note.pinned = not note.pinned
        note.save()
        serializer = self.get_serializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
