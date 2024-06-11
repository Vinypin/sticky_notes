# note\views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Post
from .forms import NoteForm, PostForm
from django.db.models import Count


def home(request):
    return render(request, 'note/home.html')


def list_notes(request):
    notes_with_comments_count = Note.objects.annotate(num_comments=Count('posts'))
    return render(request, 'note/list.html', {'notes': notes_with_comments_count})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm()
    return render(request, 'note/form.html', {'form': form})

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/form.html', {'form': form, 'note': note})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('list_notes')
    return render(request, 'note/confirm_delete.html', {'note': note})

def view_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/view.html', {'note': note})

def create_post(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.note = note
            post.save()
            return redirect('view_note', pk=note.pk)
    else:
        form = PostForm()
    return render(request, 'note/post_form.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_note', pk=post.note.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post_form.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    note_pk = post.note.pk
    if request.method == 'POST':
        post.delete()
        return redirect('view_note', pk=note_pk)
    return render(request, 'note/confirm_delete_post.html', {'post': post})
