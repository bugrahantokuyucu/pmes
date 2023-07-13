from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', include("dashboard.urls")),
    path("work_orders/", include("work_orders.urls")),
    path("machines/", include("machines.urls")),
    path("operators/", include("operators.urls")),
    path("processes/", include("processes.urls")),
    path("notes/", include("notes.urls")),
]
