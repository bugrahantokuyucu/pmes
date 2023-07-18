from django.contrib import admin
from .models import ProcessLog, CompletedPrint


admin.site.register(ProcessLog)
admin.site.register(CompletedPrint)
