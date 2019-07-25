from django.contrib import admin
from .models import news


# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'timer', 'title')


admin.site.register(news, newsAdmin)
