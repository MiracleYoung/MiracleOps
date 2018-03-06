"""MiracleCMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings
from .views import IndexView, TestLongUrlView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index', kwargs={'app': 'Dashboard'}),
    url(r'^users/', include('users.urls.views_urls', namespace='users')),
    url(r'^assets/', include('assets.urls.views_urls', namespace='assets'), kwargs={'app': 'Asset'}),
    url(r'^cms/', include('cms.urls.views_urls', namespace='cms'), kwargs={'app': 'Cluster Management'}),
    url(r'^terminals/', include('terminals.urls', namespace='terminals'), kwargs={'app': 'Terminal'}),
    url(r'^docs/', include('docs.urls', namespace='docs'), kwargs={'app': 'Doc'}),

    url(r'^api/v1/', include('api.urls.v1', namespace='api-v1')),

    url(r'test/long/url/', TestLongUrlView.as_view(), name='test-long-url'),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
