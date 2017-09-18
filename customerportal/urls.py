from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forms\/', views.forms_dashboard, name='forms'),
    # url(r'forms/create', views.create, name='create')
]