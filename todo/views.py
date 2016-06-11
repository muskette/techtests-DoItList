from django.views.generic import ListView, CreateView

from todo.forms import TodoListForm
from todo.models import TodoList


def a(request):
    pass

class TodoListListView(ListView):
    model = TodoList



# TODO: Find out why this keeps loading the list template!
class TodoListCreateView(CreateView):
    model = TodoList
    form_class = TodoListForm
    template_name = 'todo/todolist_create.html'

    def form_valid(self, form):
        todo_list = form.save(commit=False)
        todo_list.owner = self.request.user
        return todo_list.save()
