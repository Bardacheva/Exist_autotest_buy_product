import pytest

# общие функции, фикстуры, настройки для всех тестов
@pytest.fixture()
def set_up():
    print("Start test") # перед тестом

    yield # сам тест

    print("Finish test")  # после теста

