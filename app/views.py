from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import CallBack, BuyFeed, DownFeed, FooterFeed
from .forms import CallBackForm, BuyFeedForm, DownFeedForm, FooterFeedForm

from .services import send_mail


def index(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """
    if request.method == 'POST':
        form_call = CallBackForm(request.POST)
        form_buy = BuyFeedForm(request.POST)
        form_down = DownFeedForm(request.POST)
        form_footer = FooterFeedForm(request.POST)
        if form_call.is_valid():
            data = form_call.cleaned_data
            form_place = 'обратный звонок'
            feed = CallBack()
            feed.name = data['name']
            feed.phone = data['phone']
            feed.cat_form = form_place
            feed.save()
            send_mail.send_info(form_place, name=data['name'], phone=data['phone'])

        if form_buy.is_valid():
            data = form_buy.cleaned_data
            form_place = 'покупка акций'
            feed = BuyFeed()
            feed.name = data['name']
            feed.phone = data['phone']
            feed.email = data['email']
            feed.cat_form = form_place
            feed.save()
            send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

        if form_down.is_valid():
            data = form_buy.cleaned_data
            form_place = 'скачать документы'
            feed = DownFeed()
            feed.name = data['name']
            feed.phone = data['phone']
            feed.email = data['email']
            feed.cat_form = form_place
            feed.save()
            send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

        if form_footer.is_valid():
            data = form_buy.cleaned_data
            form_place = 'заявка для связи'
            feed = FooterFeed()
            feed.name = data['name']
            feed.phone = data['phone']
            feed.email = data['email']
            feed.cat_form = form_place
            feed.save()
            send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

        return render(request, 'index.html', {'form_call': form_call, 'form_buy': form_buy,
                                              'form_down':form_down, 'form_footer': form_footer})

    else:
        form_call = CallBackForm(request.POST)
        form_buy = BuyFeedForm(request.POST)
        form_down = DownFeedForm(request.POST)
        form_footer = FooterFeedForm(request.POST)

        return render(request, 'index.html', {'form_call': form_call, 'form_buy': form_buy,
                                              'form_down': form_down, 'form_footer': form_footer})
