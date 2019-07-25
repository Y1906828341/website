from django.shortcuts import render_to_response, get_object_or_404
from article.models import article
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def paginator(request, articles):
    paginator = Paginator(articles, settings.EACH_PAGE_ARTICLE_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url的页面参数（GET请求）
    page_of_articles = paginator.get_page(page_num)
    currentr_page_num = page_of_articles.number  # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 1, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 1, paginator.num_pages) + 1))
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['articles'] = page_of_articles.object_list
    context['pages'] = page_of_articles
    context['range'] = page_range
    return context


def lists(request):
    articles = article.objects.all()
    context = paginator(request, articles)
    return render_to_response('lists.html', context)


def detail(request, id):
    article_details = get_object_or_404(article, id=id)
    context = {}
    context['previous_article'] = article.objects.filter(id__gt=id).last()
    context['next_article'] = article.objects.filter(id__lt=id).first()
    context['article'] = article_details
    return render_to_response('detail.html', context)
