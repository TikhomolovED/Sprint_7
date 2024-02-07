test_create_new_order_api - проверка создания нового заказа
test_getting_list_orders_api - проверка получения списка заказов
test_login_courier_api.py - проверка логина курьера
test_login_with_uncorrect_data_api - проверка логина курьера с отсутствием полей
test_reg_double_courier_api.py - проверка создания дубля курьера
test_reg_new_courier_api - проверка регистрации нового курьера
test_reg_new_courier_without_any_data_api - проверка создания курьера с отсутствием обязательных полей
test_reg_user_same_login_api - провека создания курьера с логином который уже существует

python -m pytest  --alluredir ./allure_results - для генерации отчета allure
allure serve ./allure_results/ - составление отчета allure

