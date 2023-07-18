from django.urls import path
from . import views


urlpatterns = [
    path("<uuid:work_order_uuid>/", views.transactions, name="transactions"),
    path("<uuid:work_order_uuid>/start/", views.start_process, name="start_process"),
    path("<uuid:work_order_uuid>/cancel/", views.cancel_process, name="cancel_process"),
    path("<uuid:work_order_uuid>/pause/", views.pause_process, name="pause_process"),
    path("<uuid:work_order_uuid>/complete/", views.complete_process, name="complete_process"),
    path("<uuid:work_order_uuid>/continue/", views.continue_process, name="continue_process"),
    path("<uuid:work_order_uuid>/copy_complete/<str:number_of_remained_copy>", views.copy_complete_process,
         name="copy_complete_process"),
    path("copy_completed/<uuid:completed_print_uuid>/", views.completed_copy_detail,
         name="completed_copy_detail"),
]
