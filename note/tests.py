from django.test import TestCase
from django.urls import reverse
from .models import Note, Post

class NoteTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='Test content for the note')

    def test_list_notes(self):
        response = self.client.get(reverse('list_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertTemplateUsed(response, 'note/list.html')

    def test_create_note(self):
        response = self.client.post(reverse('create_note'), {'title': 'New Note', 'content': 'New note content'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_update_note(self):
        response = self.client.post(reverse('update_note', args=[self.note.pk]), {'title': 'Updated Note', 'content': 'Updated content'})
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)

    def test_view_note(self):
        response = self.client.get(reverse('view_note', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test content for the note')
        self.assertTemplateUsed(response, 'note/view.html')


class PostTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='Test content for the note')
        self.post = Post.objects.create(note=self.note, content='Test post content')

    def test_create_post(self):
        response = self.client.post(reverse('create_post', args=[self.note.pk]), {'content': 'New post content'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_post(self):
        response = self.client.post(reverse('update_post', args=[self.post.pk]), {'content': 'Updated post content'})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.content, 'Updated post content')

    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
