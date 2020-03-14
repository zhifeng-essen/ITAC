from django.shortcuts import render
import json
from django.http import HttpResponse
from django.db.models import Q
from rambler.models import Ingredient


# Create your views here.
def advanced(request):
    return render(request, "advanced/setcher.html")


def advanced_ajax(request):
    post_data = request.POST
    q = 'benzophenone'

    results = list(
        Ingredient.objects.filter(Q(Molecule_name__icontains=q) | Q(CAS_id__icontains=q) | Q(Alias__icontains=q)))
    data = [Ingredient.getPatialData(i.Ingredient_id)[0] for i in results]
    columns = Ingredient.getColumns()

    return HttpResponse(json.dumps({'data': data, 'columns': columns}), content_type="application/json")
