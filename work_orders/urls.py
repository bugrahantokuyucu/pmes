from django.urls import path
from . import views


urlpatterns = [
    path("", views.work_order_list, name="work_order_list"),
    path("<str:filter>/", views.work_order_list, name="work_order_filtered_list"),
    path("create/", views.work_order_create, name="work_order_create"),
    path("<int:work_order_pk>/details/", views.work_order_detail, name="work_order_detail"),
    path("<int:work_order_pk>/edit/", views.work_order_edit, name="work_order_edit"),
    path("<int:work_order_pk>/pdf/", views.create_pdf, name="create_work_order_pdf"),
    path("copy_complete/<int:copy_complete_pk>/pdf/", views.create_copy_complete_pdf, name="create_copy_complete_pdf"),
]
