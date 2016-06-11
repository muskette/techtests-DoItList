from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lists/', views.a, name="lists"),
    url(r'^lists/(?P<pk>\d+)', views.a, name="view_list"),
]
