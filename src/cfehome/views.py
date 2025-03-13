from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
  my_title = "my page"
  # esto es parte del ORM de django, basicamente al llamar .all, obtienes todos los registros de la tabla de PageVisit
  qs = PageVisit.objects.all()
  # .filter es una funcion que te filtra segun lo que le pases, en este caso filtramos las queries que se hagan a la pagina actual con request
  page_qs = PageVisit.objects.filter(path=request.path)
  payload = {
    "page_title": my_title,
    "page_visit_count": page_qs.count(),
    "percent": (page_qs.count() * 100.0) / qs.count(),
    "total_visit_count": qs.count()
  }
  html_template = "home.html"
  PageVisit.objects.create(path=request.path)
  return render(request, html_template, payload)