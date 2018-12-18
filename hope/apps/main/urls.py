from django.conf.urls import url
from django.contrib.auth import views as auth_views

from hope.apps.main import views as main_views


urlpatterns = [
    url(r'^$', main_views.index),
]
