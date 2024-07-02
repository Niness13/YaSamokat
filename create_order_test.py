# Нина Кузьмина, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def create_order():
    current_body = data.order_body.copy()
    track_number = sender_stand_request.post_new_order(current_body)
    return str(track_number.json()["track"])
def positive_assert():
# Выполнить запрос на создание заказа. [create_order()]
# Сохранить номер трека заказа. [track_number = ...]
    track_number = create_order()

# Выполнить запрос на получения заказа по треку заказа.
    current_param = data.get_order_parameters.copy()
    current_param["t"] = track_number
    response = sender_stand_request.get_order(current_param)

# Проверить, что код ответа равен 200.
    assert response.status_code == 200

def test_order():
    positive_assert()
