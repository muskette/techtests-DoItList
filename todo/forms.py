from django.forms import ModelForm


class TodoListForm(ModelForm):
    class Meta:
        exclude = ['owner']
