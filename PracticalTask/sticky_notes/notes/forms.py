"""
forms.py

This module defines the forms used in the Sticky Notes application.
It contains NoteForm, a ModelForm used to create or update Note instances
via templates.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note instances.

    This form uses the Note model and includes the title and content fields.

    Attributes:
        title (str): The title of the note.
        content (str): The main content/body of the note.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
