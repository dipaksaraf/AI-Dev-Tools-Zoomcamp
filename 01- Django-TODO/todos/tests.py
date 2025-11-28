# todos/tests.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Todo
from .forms import TodoForm

class TodoModelTests(TestCase):
    def test_create_todo_and_str(self):
        t = Todo.objects.create(
            title="Test task",
            description="A short description",
            due_date=timezone.now() + timedelta(days=1),
        )
        self.assertEqual(str(t), "Test task")
        self.assertIsNotNone(t.created_at)
        self.assertFalse(t.resolved)

    def test_get_absolute_url(self):
        t = Todo.objects.create(title="URL task")
        url = t.get_absolute_url()
        self.assertIn(str(t.pk), url)

    def test_toggle_resolved_persists(self):
        t = Todo.objects.create(title="Toggle me")
        self.assertFalse(t.resolved)
        t.resolved = True
        t.save()
        t.refresh_from_db()
        self.assertTrue(t.resolved)


class TodoFormTests(TestCase):
    def test_form_valid_with_datetime_local_format(self):
        # Browser sends 'YYYY-MM-DDTHH:MM' for datetime-local
        dt = (timezone.now() + timedelta(days=2)).replace(second=0, microsecond=0)
        data = {
            'title': 'Form Task',
            'description': 'desc',
            'due_date': dt.strftime('%Y-%m-%dT%H:%M'),
            'resolved': False,
        }
        form = TodoForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_title(self):
        form = TodoForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class TodoViewsIntegrationTests(TestCase):
    def setUp(self):
        # create a sample todo
        self.todo = Todo.objects.create(
            title="View Task",
            description="for views",
            due_date=timezone.now() + timedelta(days=1),
        )

    def test_list_view_status_and_contains_todo(self):
        url = reverse('todos:todo-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.todo.title)

    def test_detail_view(self):
        url = reverse('todos:todo-detail', args=[self.todo.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.todo.title)

    def test_create_view_post_creates(self):
        url = reverse('todos:todo-add')
        data = {
            'title': 'Created via test',
            'description': 'desc',
            'due_date': (timezone.now() + timedelta(days=3)).strftime('%Y-%m-%dT%H:%M'),
            'resolved': False,
        }
        resp = self.client.post(url, data, follow=True)
        # should redirect to detail or list; ultimately object count increases
        self.assertEqual(Todo.objects.filter(title='Created via test').count(), 1)
        self.assertIn(resp.status_code, (200, 302))

    def test_update_view_post_updates(self):
        url = reverse('todos:todo-edit', args=[self.todo.pk])
        new_title = 'Updated Title'
        data = {
            'title': new_title,
            'description': self.todo.description,
            'due_date': (self.todo.due_date or timezone.now()).strftime('%Y-%m-%dT%H:%M'),
            'resolved': self.todo.resolved,
        }
        resp = self.client.post(url, data, follow=True)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, new_title)
        self.assertIn(resp.status_code, (200, 302))

    def test_delete_view_posts_deletes(self):
        url = reverse('todos:todo-delete', args=[self.todo.pk])
        resp = self.client.post(url, follow=True)
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(pk=self.todo.pk)
        self.assertIn(resp.status_code, (200, 302))

    def test_toggle_resolved_post_toggles(self):
        url = reverse('todos:todo-toggle-resolved', args=[self.todo.pk])
        # ensure initial
        self.assertFalse(self.todo.resolved)
        resp = self.client.post(url, follow=True)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)
        # toggle back
        resp = self.client.post(url, follow=True)
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.resolved)

    def test_toggle_resolved_get_does_not_toggle(self):
        url = reverse('todos:todo-toggle-resolved', args=[self.todo.pk])
        resp = self.client.get(url)
        # your toggle view is decorated for POST only — Django will return 405 or redirect.
        # Accept 405/302/200 depending on implementation. Ensure resolved didn't change.
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.resolved)


# Optional: if you later add a property is_overdue, write a test like:
# class OverdueTests(TestCase):
#     def test_is_overdue_returns_true_for_past_due_unresolved(self):
#         past = Todo.objects.create(title="past", due_date=timezone.now() - timedelta(days=1), resolved=False)
#         self.assertTrue(past.is_overdue)