from django.contrib import admin

# Register your models here.
from .models import Storge_file,Mytext

@admin.register(Storge_file)
class Storge_fileAdmin(admin.ModelAdmin):
    pass
@admin.register(Mytext)
class MytextAdmin(admin.ModelAdmin):
    pass
