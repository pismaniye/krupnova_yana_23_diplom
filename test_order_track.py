# Яна Крупнова, 23-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_and_get_order_by_track():
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)

    # Проверяем, что заказ создался успешно (код 201)
    assert create_response.status_code == 201

    # Шаг 2: Сохранение номера трека заказа
    track_number = create_response.json()["track"]

    # Шаг 3: Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)

    # Шаг 4: Проверяем, что код ответа равен 200
    assert get_response.status_code == 200

    # Дополнительная проверка, что в ответе содержится информация о заказе
    assert get_response.json()["order"]["track"] == track_number