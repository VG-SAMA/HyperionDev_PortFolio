from django.urls import path
from .views import create_note, delete_note, get_note, update_note, note_list

urlpatterns = [
    path("", note_list, name="notes_list"),
    path("note/<int:pk>/", get_note, name="get_note"),
    path("note/edit/<int:pk>/", update_note, name="update_note"),
    path("note/new/", create_note, name="create_note"),
    path("note/<int:pk>/delete/", delete_note, name="delete_note"),
]


"""
This file defines all URL patterns for the Notes application, mapping
URLs to the corresponding views.

Routes:
- ''                     : notes_list       -> Displays all notes with search functionality
- 'note/<int:pk>/'       : get_note         -> Shows details of a specific note
- 'note/edit/<int:pk>/'  : update_note      -> Provides a form to edit a specific note
- 'note/new/'            : create_note      -> Provides a form to create a new note
- 'note/<int:pk>/delete/': delete_note      -> Confirms and deletes a specific note
"""
