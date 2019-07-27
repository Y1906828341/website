from .models import article
import xadmin


# Register your models here.
class articleAdmin(object):
    list_display = ('id', 'title', 'types')


xadmin.site.register(article, articleAdmin)
