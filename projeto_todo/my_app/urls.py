from django.urls import path
from .views import aluno_view

urlpatterns = [
    path('aluno/', aluno_view, name='aluno')
]