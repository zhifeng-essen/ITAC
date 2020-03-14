from django.shortcuts import render
import json
from django.http import HttpResponse
from django.db.models import Q
from rambler.models import Prescription, Herb, Ingredient, Target, Disease


# Create your views here.
def search(request):
    return render(request, 'search/search.html')


def search_ajax(request):
    post_data = request.POST
    q = post_data['key']
    data = []
    columns = []

    if post_data['table_name'] == 'Prescription':
        results = list(Prescription.objects.filter(Q(Chinese_name__icontains=q) | Q(Pinyin_name__icontains=q)))
        data = [Prescription.getPatialData(i.Prescription_id)[0] for i in results]
        columns = Prescription.getColumns()
    elif post_data['table_name'] == 'Herb':
        results = list(Herb.objects.filter(
            Q(Chinese_name__icontains=q) | Q(Pinyin_name__icontains=q) | Q(English_name__icontains=q) | Q(
                Latin_name__icontains=q)))
        data = [Herb.getPatialData(i.Herb_id)[0] for i in results]
        columns = Herb.getColumns()
    elif post_data['table_name'] == 'Ingredient':
        results = list(
            Ingredient.objects.filter(Q(Molecule_name__icontains=q) | Q(CAS_id__icontains=q) | Q(Alias__icontains=q)))
        data = [Ingredient.getPatialData(i.Ingredient_id)[0] for i in results]
        columns = Ingredient.getColumns()
    elif post_data['table_name'] == 'Target':
        results = list(Target.objects.filter(
            Q(Gene_symbol__icontains=q) | Q(Gene_name__icontains=q) | Q(Protein_name__icontains=q) | Q(
                Ensembl_id__icontains=q) | Q(Alias__icontains=q)))
        data = [Target.getPatialData(i.Target_id)[0] for i in results]
        columns = Target.getColumns()
    elif post_data['table_name'] == 'Disease':
        results = list(Disease.objects.filter(Q(Disease_name__icontains=q) | Q(Alias__icontains=q)))
        data = [Disease.getPatialData(i.Disease_id)[0] for i in results]
        columns = Disease.getColumns()

    return HttpResponse(json.dumps({'data': data, 'columns': columns}), content_type="application/json")


def search_th(request):
    post_data = request.POST
    resp = {}
    return HttpResponse(json.dumps(resp), content_type="application/json")
