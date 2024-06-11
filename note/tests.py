# note/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note, Post

class NoteViewTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='Test Content')

    def test_list_notes(self):
        response = self.client.get(reverse('list_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertTemplateUsed(response, 'note/list.html')

    def test_create_note(self):
        response = self.client.post(reverse('create_note'), {'title': 'New Note', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_notes'))
        self.assertEqual(Note.objects.count(), 2)

    def test_view_note(self):
        response = self.client.get(reverse('view_note', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertTemplateUsed(response, 'note/view.html')

    def test_update_note(self):
        response = self.client.post(reverse('update_note', args=[self.note.pk]), {'title': 'Updated Note', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_notes'))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_notes'))
        self.assertEqual(Note.objects.count(), 0)

class PostViewTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_list_posts(self):
        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'note/list_posts.html')

    def test_create_post(self):
        response = self.client.post(reverse('create_post'), {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_posts'))
        self.assertEqual(Post.objects.count(), 2)

    def test_view_post(self):
        response = self.client.get(reverse('view_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'note/view_post.html')

    def test_update_post(self):
        response = self.client.post(reverse('update_post', args=[self.post.pk]), {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_posts'))
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_posts'))
        self.assertEqual(Post.objects.count(), 0)
