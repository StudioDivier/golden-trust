from django.core.mail import send_mail
from django.conf import settings


def send_info(*args, **kwargs):
    SUBJECT = 'GOLD-TRUST: Новая заявка!'

    TEXT_MESASGE = 'GOLD-TRUST: пришла новая заявка по модулю  <{}>\n' \
                   'Контактные дланные: {}'.format(args[0], kwargs)

    send_mail(SUBJECT, TEXT_MESASGE, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

    return True
