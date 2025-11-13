'''
views.py

This module defines the view functions for the Notes application.
It handles the main CRUD operations for Note objects, including:
- Displaying a list of all notes with optional search functionality
- Viewing the details of a specific note
- Creating new notes
- Updating existing notes
- Deleting notes

Each view interacts with the Note model and its corresponding templates
to render dynamic HTML pages for user interaction.

References:
https://docs.djangoproject.com/en/5.0/topics/testing/overview/
https://docs.djangoproject.com/en/5.2/topics/testing/advanced/
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Testing
'''

from django.test import TestCase
from django.urls import reverse
from .models import Note


class TestNotesModel(TestCase):
    """Unit tests for the Note model."""

    def setUp(self):
        """Create sample Note instances for testing."""
        Note.objects.create(title='TestingNote', content='TestingNoteContent')
        Note.objects.create(title='Note2', content='Content1')

    def test_note_has_title(self):
        """Verify that a Note instance has the correct title."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'TestingNote')
        # self.assertEqual(note.content, 'TestingNoteContent')

    def test_note_has_content(self):
        """Verify that a Note instance has the correct content."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'TestingNoteContent')

    def test_delete_note(self):
        """Ensure that a Note can be deleted successfully."""
        note = Note.objects.get(id=2)
        self.assertEqual(note.title, 'Note2')
        note.delete()

        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=2)

    def test_note_update(self):
        """Confirm that updating a Note's fields saves correctly."""
        note = Note.objects.get(id=1)
        note.title = 'NewTitle'
        note.save()

        update_note = Note.objects.get(id=1)
        self.assertEqual(update_note.title, 'NewTitle')

        # this is used for testing to make sure its not the same original name
        # self.assertEqual(update_note.title, 'TestingNote')


class TestNoteView(TestCase):
    """Integration tests for Note-related views."""

    def setUp(self):
        """Create sample Note instances for view testing."""
        Note.objects.create(title='TestingNote', content='TestingNoteContent')
        Note.objects.create(title='Note2', content='Content1')

    def test_note_list_view(self):
        """Test that the notes list view loads and renders all notes."""
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'TestingNote')
        self.assertContains(response, 'Note2')

        self.assertTemplateUsed(response, 'notes/notes_list.html')

    def test_note_detail_view(self):
        """Test that the note detail view displays the correct note content."""
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('get_note', args=[str(note.pk)]))

        self.assertContains(response, 'TestingNote')
        self.assertContains(response, 'TestingNoteContent')

        self.assertTemplateUsed(response, 'notes/note_detail.html')
