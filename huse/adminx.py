import xadmin
from .models import news


# Register your models here.
class newsAdmin(object):
    list_display = ('id', 'timer', 'title')


xadmin.site.register(news, newsAdmin)
