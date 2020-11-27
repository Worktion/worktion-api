from django.contrib import admin
from .models import Routine, ExecutionBlock, ExecutionExercise

# Register your models here.
admin.site.register(Routine)
admin.site.register(ExecutionBlock)
admin.site.register(ExecutionExercise)
