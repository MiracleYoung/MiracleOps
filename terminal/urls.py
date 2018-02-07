from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TerminalListView.as_view(), name='list', kwargs={'path1': 'List'}),
    url(r'^detail/$', views.TerminalDetailView.as_view(), name='detail', kwargs={'path1': 'Detail'}),
]
