from django.contrib import admin
from notes.models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'pinned', 'created_at']
    list_filter = ['pinned', 'owner']
    search_fields = ['title', 'content']
