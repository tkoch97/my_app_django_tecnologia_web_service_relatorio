from django.shortcuts import render
from django.http import HttpResponse

def aluno_view(request):
  return HttpResponse("Resultado aula prática ok")
