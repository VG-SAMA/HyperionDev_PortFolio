"""
models.py

This module defines the database models for the Sticky Notes application.
It contains the Note model which stores information about individual notes,
including title, content, creation date, and last update timestamp.
"""

from django.db import models


class Note(models.Model):
    """
    Represents a note created by the user.

    Attributes:
        title (str): The title of the note (max length 100 characters).
        content (str): The main content/body of the note.
        created_at (datetime): Timestamp when the note was created (auto-set
        on creation).
        updated_on (datetime): Timestamp when the note was last updated
        (auto-updated on save).
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human-readable string representation of the note.

        Returns:
            str: The title of the note.
        """
        return self.title
