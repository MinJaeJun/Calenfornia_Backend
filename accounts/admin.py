from django.contrib import admin
from .models import Classnet, User
# Register your models here.

@admin.register(User)
class UserAmin(admin.ModelAdmin):
    pass


@admin.register(Classnet)
class ClassnetAmin(admin.ModelAdmin):
    pass