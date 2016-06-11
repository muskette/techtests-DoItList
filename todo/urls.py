from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lists/', views.TodoListListView.as_view(), name="lists"),
    url(r'^lists/create$', views.TodoListCreateView.as_view(), name="list_create"),
    url(r'^lists/(?P<pk>\d+)', views.a, name="view_list"),
]
