import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import DynamicModel


def front_page(request):
    data = DynamicModel.objects.all().order_by("model_name")
    return render(request, "front_page.html", {"data": data})


@csrf_exempt
def import_data(request):
    if request.method == "POST":
        try:
            DynamicModel.objects.all().delete()

            data = json.loads(request.body)

            for item in data:
                model_name = list(item.keys())[0]
                model_data = item[model_name]
                DynamicModel.objects.create(model_name=model_name, data=model_data)

            return HttpResponse("Data imported successfully", status=201)

        except Exception as e:
            return HttpResponse(f"Error importing data: {str(e)}", status=500)
    else:
        return HttpResponse("Method not allowed", status=405)


def create_html_table(data):
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    table_html = "<table>"
    table_html += "<tr>"
    for key in all_keys:
        table_html += f"<th>{key}</th>"
    table_html += "</tr>"
    for item in data:
        table_html += "<tr>"
        for key in all_keys:
            table_html += f"<td>{item.get(key, '')}</td>"
        table_html += "</tr>"
    table_html += "</table>"
    return table_html


def get_detail_model_name(request, model_name):
    queryset = DynamicModel.objects.filter(model_name=model_name)
    data = [obj.data for obj in queryset]

    if not data:
        return HttpResponse({"Requested endpoint does not exist"}, status=404)
    
    val = create_html_table(data)

    return render(request, "template.html", {"data": val})

def get_detail_with_id(request, model_name, content_id):
    queryset = DynamicModel.objects.filter(model_name=model_name)
    queryset = queryset.filter(data__id=content_id)
    data = [obj.data for obj in queryset]
    if not data:
        return HttpResponse({"Requested endpoint does not exist"}, status=404)
    
    val = create_html_table(data)

    return render(request, "template.html", {"data": val})