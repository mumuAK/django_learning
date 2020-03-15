from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article
from django.core.paginator import Paginator

# Create your views here.

def hello_world(request):
    return HttpResponse("hello world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date

    return_str = 'title: %s, brief_content:%s' \
                 'content:%s, atricle_is: %s, publish-date: %s ' % (title,
                                                                    brief_content,
                                                                    content,
                                                                    article_id,
                                                                    publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    page_index  = request.GET.get('page')
    if page_index:
        page_index = int(page_index)
    else:
        page_index = 1
    print('page', page_index)

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]
    paginator = Paginator(all_article, 5)
    page_num = paginator.num_pages
    print('page_num:', paginator.num_pages)
    page_article_list = paginator.page(page_index)
    if page_article_list.has_next():
        next_page = page_index + 1
    else:
        next_page = page_index

    if page_article_list.has_previous():
        pre_page = page_index - 1
    else:
        pre_page = page_index

    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'cur_page': page_index,
                      'pre_page': pre_page,
                      'next_page': next_page,
                      'top5_article_list': top5_article_list,
                  }
                  )


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    cur_article = None
    pre_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if article.article_id == article_id:
            if index == 0:
                pre_index = len(all_article) - 1
                next_index = index + 1
            elif index == len(all_article) - 1:
                pre_index = index - 1
                next_index = 0
            else:
                pre_index = index - 1
                next_index = index + 1

            cur_article = article
            pre_article = all_article[pre_index]
            next_article = all_article[next_index]
            break

    section_list = cur_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'current_article': cur_article,
                      'section_list': section_list,
                      'pre_article': pre_article,
                      'next_article': next_article,
                  }
                  )
