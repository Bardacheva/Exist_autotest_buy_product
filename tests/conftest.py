import pytest

# общие функции, фикстуры, настройки для всех тестов
@pytest.fixture()
def set_up():
    print("Start test") # перед тестом

    yield # сам тест

    print("Finish test")  # после теста


# общие функции, фикстуры, настройки для всех тестов
@pytest.fixture(scope="module") # запускается для всего модуля
def set_group():
    print("Enter system") # перед тестом

    yield # сам тест

    print("Exit system")  # после теста