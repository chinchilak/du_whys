import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import DynamicModel


def blank_page(request):
    return render(request, "blank.html")

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

def get_detail_model_name(request, model_name):
    queryset = DynamicModel.objects.filter(model_name=model_name)
    data = [obj.data for obj in queryset]
    if not data:
        return HttpResponse({"Requested endpoint does not exist"}, status=404)
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")

def get_detail_with_id(request, model_name, content_id):
    queryset = DynamicModel.objects.filter(model_name=model_name)
    queryset = queryset.filter(data__id=content_id)
    data = [obj.data for obj in queryset]
    if not data:
        return HttpResponse({"Requested endpoint does not exist"}, status=404)
    return HttpResponse(json.dumps(data[0], ensure_ascii=False), content_type="application/json")
