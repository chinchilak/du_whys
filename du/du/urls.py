from django.urls import path
from api.views import blank_page, import_data, get_detail_model_name, get_detail_with_id

urlpatterns = [
    path("", blank_page, name="blank_page"),
    path("import/", import_data, name="import_data"),
    path("detail/<str:model_name>/", get_detail_model_name, name="get_detail_model_name"),
    path("detail/<str:model_name>/<int:content_id>/", get_detail_with_id, name="get_detail_with_id"),
]
