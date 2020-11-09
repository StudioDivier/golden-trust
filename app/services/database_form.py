from ..models import CallBack, BuyFeed, DownFeed, FooterFeed


def callback_add(**kwargs):
    try:
        data = CallBack(kwargs)
        data.save()
        return True
    except Exception:
        return False


def buyfeed(**kwargs):
    try:
        data = BuyFeed(kwargs)
        data.save()
        return True
    except Exception:
        return False


def downfeed(**kwargs):
    try:
        data = DownFeed(kwargs)
        data.save()
        return True
    except Exception:
        return False


def footerfeed(**kwargs):
    try:
        data = FooterFeed(kwargs)
        data.save()
        return True
    except Exception:
        return False
