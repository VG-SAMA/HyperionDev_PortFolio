"""
views.py

This module defines all the views for the Sticky Notes application.
It handles displaying, creating, updating, and deleting notes, as well as
searching through existing notes.

Functions:
-----------
note_list(request):
    Retrieves all notes or filters them based on a search query.

get_note(request, pk):
    Retrieves and displays a specific note by its primary key.

create_note(request):
    Handles the creation of a new note using a Django form.

update_note(request, pk):
    Handles updating an existing notes title and content.

delete_note(request, pk):
    Handles deleting a specific note from the DB.


Reference:
https://www.youtube.com/watch?v=AGtae4L5BbI
https://docs.djangoproject.com/en/5.1/topics/db/queries/#retrieving-specific-objects-with-filters

"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.db.models import Q


def note_list(request):
    """
    Displays a list of all notes, with optional search functionality.

    Parameters:
    - request: HttpRequest object containing GET data (for search queries).

    Behavior:
    - Retrieves all Note objects from the database.
    - Checks if a search query ('q') exists in the GET parameters.
    - If a query exists, filters the notes by title or content
        (case-insensitive).
    - Renders the notes list template with either all notes or filtered notes.
    """
    query = request.GET.get("q")
    all_notes = Note.objects.all()

    context = {"notes": all_notes, "page_title": "All Notes"}

    # filter query based on search in template if not empty
    if query:
        notes = all_notes.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        # return the filtered query set
        return render(
            request,
            "notes/notes_list.html",
            {"notes": notes, "page_title": f'Search results for "{query}" '},
        )
    # return all notes
    return render(request, "notes/notes_list.html", context)


def get_note(request, pk):
    """
    Retrieves a single Note object based on its primary key and displays its
    details.

    Parameters:
    - request: HttpRequest object (usually GET).
    - pk: Primary key of the Note to retrieve.

    Behavior:
    - Attempts to fetch the Note from the database using the provided primary
    key.
    - If the Note does not exist, raises a 404 error.
    - Renders the note_detail template with the retrieved note.
    """
    this_note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": this_note})


def create_note(request):
    """
    Handles creating a new Note object in the database.

    Parameters:
    - request: HttpRequest object containing POST data for the new note.

    Behavior:
    - If the request method is POST, binds the submitted data to a NoteForm.
    - Validates the form, saves the Note to the database, and redirects to the
    notes list.
    - If the request method is GET, displays an empty form for creating a new
    note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("notes_list")

    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def update_note(request, pk):
    """
    Updates an existing Note object in the DB.

    Parameters:
    - request: HttpRequest object containing GET or POST data.
    - pk: Primary key of the Note to update.

    Behavior:
    - Retrieves the Note instance based on the primary key.
    - If the request method is POST, binds the submitted data to a NoteForm.
    - Validates the form and saves changes to the DB.
    - Redirects the user to the list of all notes upon successful update.
    - If the request is GET, displays the form pre-filled with the note's
    current data.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("notes_list")

    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def delete_note(request, pk):
    """
    Deletes a Note object from the DB after confirmation.

    Parameters:
    - request: HttpRequest object containing GET or POST data.
    - pk: Primary key of the Note to delete.

    Behavior:
    - Retrieves the Note instance based on the primary key.
    - If the request method is POST, deletes the Note from the DB.
    - Redirects the user to the list of all notes upon successful deletion.
    - If the request is GET, displays a confirmation page before deletion.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("notes_list")

    return render(request, "notes/confirm_delete.html", {"note": note})
