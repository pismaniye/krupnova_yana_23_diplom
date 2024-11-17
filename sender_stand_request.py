import requests
import configuration

def post_new_order(order_body):
    """
    Создание нового заказа
    :param order_body: тело запроса для создания заказа
    :return: ответ сервера
    """
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=order_body)

def get_order_by_track(track_number):
    """
    Получение заказа по его трек-номеру
    :param track_number: номер трека заказа
    :return: ответ сервера
    """
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                       params={"t": track_number})