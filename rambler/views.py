from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Prescription, Herb, Ingredient, Target, Disease


# Create your views here.
def index(request):
    return render(request, 'rambler/index/index.html')


def browse(request):
    return render(request, 'rambler/browse/lists.html')


def browse_ajax(request):
    post_data = request.POST

    def get_res(Table):
        total = len(Table.objects.all())
        start = int(post_data['page_size']) * int(post_data['page_num'])
        data = []
        for i in range(start - 14, start + 1):
            data.append(Table.getPatialData(i)[0])
        columns = Table.getColumns()
        return {"Total": total, "Data": data, "columns": columns}

    if post_data['table_name'] == 'Prescription':
        resp = get_res(Prescription)
    elif post_data['table_name'] == 'Herb':
        resp = get_res(Herb)
    elif post_data['table_name'] == 'Ingredient':
        resp = get_res(Ingredient)
    elif post_data['table_name'] == 'Target':
        resp = get_res(Target)
    elif post_data['table_name'] == 'Disease':
        resp = get_res(Disease)

    return HttpResponse(json.dumps(resp), content_type="application/json")


def detail(request, ID):
    if ID[:2] == 'PN':
        return render(request, 'rambler/browse/details_Prescription.html')
    elif ID[:2] == 'HB':
        herb = Herb.objects.get(ID=ID)
        return render(request, 'rambler/browse/details_Herb.html', {'herb': herb})
    elif ID[:2] == 'IT':
        ingredient = Ingredient.objects.get(ID=ID)
        return render(request, 'rambler/browse/details_Ingredient.html', {'ingredient': ingredient})
    elif ID[:2] == 'TT':
        return render(request, 'rambler/browse/details_Target.html')
    elif ID[:2] == 'DE':
        return render(request, 'rambler/browse/details_Disease.html')


def detail_ajax(request):
    post_data = request.POST
    data, columns = [], []

    if post_data['rrid'][:2] == 'PN':
        pass
    elif post_data['rrid'][:2] == 'HB':
        if post_data['table_name'] == 'Ingredient':
            data = [Ingredient.getPatialData(i.Ingredient_id)[0] for i in
                    list(Herb.objects.get(ID=post_data['rrid']).ingredients.all())]
            columns = Ingredient.getColumns()
    elif post_data['rrid'][:2] == 'IT':
        if post_data['table_name'] == 'Herb':
            data = [Herb.getPatialData(i.Herb_id)[0] for i in
                    list(Ingredient.objects.get(ID=post_data['rrid']).herb_set.all())]
            columns = Herb.getColumns()
        if post_data['table_name'] == 'Target':
            data = [Target.getPatialData(i.Target_id)[0] for i in
                    list(Ingredient.objects.get(ID=post_data['rrid']).targets.all())]
            columns = Target.getColumns()
    elif post_data['rrid'][:2] == 'TT':
        pass
    elif post_data['rrid'][:2] == 'DT':
        pass

    return HttpResponse(json.dumps({'data': data, 'columns': columns}), content_type="application/json")
