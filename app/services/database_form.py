from ..models import CallBack


def add_feed_to_db(name: str, phone: str, cat_form: str):
    """
    Функция добавления записи из формы в БД
    :param name: имя польлзователя
    :param email: почта заявителя
    :param form: название или нахождение формы
    :return: True
    """
    try:
        feed = CallBack()
        feed.name = name
        feed.telephone = phone
        feed.cat_form = cat_form
        feed.save()
        return True

    except BaseException:
        return False