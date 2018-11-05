from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from DB import db_config

from django.views import View


class IndexView(View):
    """首页"""

    def get(self, request):
        db_config_ = db_config.DB_helper()
        massages = db_config_.select_title()
        keys = ['id', 'username', 'sex', 'experience']
        contacts, part_page = pagination(request, massages, keys, 5)
        return render(request, 'index.html', {'contacts': contacts, 'part_page': part_page})


def pagination(request, massages, keys, per_page_num):
    '''
    数据分页
    :param massages: 多维列表或元组
    :param keys: 列表或元组对应值（需与其相对于）
    :param per_page_num: 每一页显示数据条数
    :return: 每一页数据：contacts, 翻页数字标签：part_page
    '''
    list_json = [dict(zip(keys, item)) for item in massages]
    paginator = Paginator(list_json, per_page_num)  # 每页显示5条数据

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        contacts = paginator.page(page)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    if int(page) < 6:
        P = 5
    elif int(page) >= int(paginator.num_pages) - 1:
        P = int(paginator.num_pages) - 3
    else:
        P = page

    part_page = [i for i in range(int(P) - 3, int(P) + 3)]

    return contacts, part_page
