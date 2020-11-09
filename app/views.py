from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import CallBackForm, BuyFeedForm, DownFeedForm, FooterFeedForm

from .services import send_mail
from .services import database_form


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

        if 'simple-callback' in request.POST:
            # form_call = CallBackForm(request.POST)
            if form_call.is_valid():
                data = form_call.cleaned_data
                form_place = 'обратный звонок'
                bd_tg = database_form.callback_add(name=data['name'], phone=data['phone'],
                                                   cat_form=form_place)
                send_mail.send_info(form_place, name=data['name'], phone=data['phone'])

            return render(request, 'thanks.html')

        if 'buy-stocks' in request.POST:
            # form_buy = BuyFeedForm(request.POST)
            if form_buy.is_valid():
                data = form_buy.cleaned_data
                form_place = 'покупка акций'
                bd_tg = database_form.callback_add(name=data['name'], phone=data['phone'],
                                                   email=data['email'], cat_form=form_place)
                send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

            return HttpResponseRedirect('/thanks')

        if 'download-documents' in request.POST:
            # form_down = DownFeedForm(request.POST)
            if form_down.is_valid():
                data = form_down.cleaned_data
                form_place = 'скачать документы'
                database_form.callback_add(name=data['name'], phone=data['phone'],
                                                   email=data['email'], cat_form=form_place)
                send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

            return HttpResponseRedirect('/thanks')

        if 'footer-form' in request.POST:
            # form_footer = FooterFeedForm(request.POST)
            if form_footer.is_valid():
                data = form_footer.cleaned_data
                form_place = 'заявка для связи'
                database_form.callback_add(name=data['name'], phone=data['phone'],
                                                   email=data['email'], cat_form=form_place)
                send_mail.send_info(form_place, name=data['name'], phone=data['phone'], email=data['email'])

            return HttpResponseRedirect('/thanks')

    else:
        form_call = CallBackForm(request.POST)
        form_buy = BuyFeedForm(request.POST)
        form_down = DownFeedForm(request.POST)
        form_footer = FooterFeedForm(request.POST)

        return render(request, 'index.html', {'form_call': form_call, 'form_buy': form_buy,
                                              'form_down': form_down, 'form_footer': form_footer})


def thank(request):
    return render(request, 'thanks.html')


def privacy(request):
    return render(request, 'privacy.html')

