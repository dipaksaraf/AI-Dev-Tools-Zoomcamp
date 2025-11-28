from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todos:todo-list')

# Toggle resolved via POST (small view)
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(require_POST, name='dispatch')
class ToggleResolvedView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.resolved = not todo.resolved
        todo.save()
        return redirect(request.META.get('HTTP_REFERER', todo.get_absolute_url()))
