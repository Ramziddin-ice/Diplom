from django.contrib import admin

# Register your models here.
from .models import Shingle_model,Shingle_text_model,Textbase

@admin.register(Shingle_text_model)
class Shingle_text_modelAdmin(admin.ModelAdmin):
    pass
@admin.register(Shingle_model)
class Shingle_modelAdmin(admin.ModelAdmin):
    pass
@admin.register(Textbase)
class TextbaseAdmin(admin.ModelAdmin):
    pass
