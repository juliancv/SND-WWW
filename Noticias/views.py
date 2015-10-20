from django.shortcuts import render, render_to_response
from django.db.models import Q
from .models import Noticia

# Create your views here.

def search(request):
	query = request.GET.get('q','')
	if query:
		qset = (
			Q(titulo__icontains = query)
		)
		results = Noticia.objects.filter(qset).distinct()
	else:
		results = []

	return render_to_response("Noticias/search.html",{
		"results": results,
		"query": query
		})

