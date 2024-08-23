import time
from playwright.sync_api import Page, expect


def test_login_form_1(page: Page):
    page.goto("http://localhost:3000/welcome")
    print("Не авторизованный пользователь пытается получить доступ к контенту по эндпоинту /welcome")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Вернулись к форме авторизации")


def test_login_form_2(page: Page):
    user_name = "aqa"
    password = "AQA123"

    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    expect(page.get_by_text('Вы авторизовались')).to_be_visible()
    print("Проверили, что отобразилось \"Вы авторизовались\"")

    page.get_by_role("button", name="Logout").click()
    print("Клик по кнопке Logout")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")


def test_login_form_3(page: Page):
    user_name = "test"
    password = "test123"

    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    expect(page.get_by_text('Вы авторизовались')).to_be_visible()
    print("Проверили, что отобразилось \"Вы авторизовались\"")

    page.get_by_role("button", name="Logout").click()
    print("Клик по кнопке Logout")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")


def test_login_form_4(page: Page):
    user_name = "admin"
    password = "admin"

    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    expect(page.get_by_text('Вы авторизовались')).to_be_visible()
    print("Проверили, что отобразилось \"Вы авторизовались\"")

    page.get_by_role("button", name="Logout").click()
    print("Клик по кнопке Logout")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")


def test_login_form_5(page: Page):
    user_name = "testfake"
    password = "test123"

    print("Тест не корректный user-name")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name не валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    page.get_by_role("button", name="Login").click()
    expect(page.locator('#message')).to_have_text('User not found')
    print("Проверка прошла успешно, итоговый результат User not found")


def test_login_form_6(page: Page):
    user_name = "aqa"
    password = "admin"

    print("Тест не корректный password")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password не валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    page.get_by_role("button", name="Login").click()
    expect(page.locator('#message')).to_have_text('Incorrect password')
    print("Проверка прошла успешно, итоговый результат Incorrect password")


def test_login_form_7(page: Page):
    user_name = "aqa "
    password = "AQA123"
    print("Проверим корректные значения с пробелом в user-name")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением с пробелом: {user_name}_")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    expect(page.get_by_text('Вы авторизовались')).to_be_visible()
    print("Проверили, что отобразилось \"Вы авторизовались\"")

    page.get_by_role("button", name="Logout").click()
    print("Клик по кнопке Logout")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")


def test_login_form_8(page: Page):
    user_name = "aqa"
    password = " AQA123"
    print("Проверим корректные значения с пробелом в password")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением с пробелом: _{password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    expect(page.get_by_text('Вы авторизовались')).to_be_visible()
    print("Проверили, что отобразилось \"Вы авторизовались\"")

    page.get_by_role("button", name="Logout").click()
    print("Клик по кнопке Logout")

    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")


def test_login_form_9(page: Page):
    user_name = ""
    password = "AQA123"
    print("Протестируем пустой user-name")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    print("Запускаем проверку на валидацию пустых полей")
    expect(page.locator('#message')).to_have_text('fill in the required form fields')
    print("Проверка прошла успешно, итоговый результат fill in the required form fields")


def test_login_form_10(page: Page):
    user_name = "aqa"

    print("Протестируем пустой password")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    print("Запускаем проверку на валидацию пустых полей")
    expect(page.locator('#message')).to_have_text('fill in the required form fields')
    print("Проверка прошла успешно, итоговый результат fill in the required form fields")


def test_login_form_11(page: Page):
    user_name = ""
    password = ""
    print("Протестируем пустые поля")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(user_name)
    print(f"Заполняем поле user-name валидным значением: {user_name}")
    page.locator("#password").fill(password)
    print(f"Заполняем поле password валидным значением: {password}")

    page.get_by_role("button", name="Login").click()
    print("Клик по кнопке Login")

    print("Запускаем проверку на валидацию пустых полей")
    expect(page.locator('#message')).to_have_text('fill in the required form fields')
    print("Проверка прошла успешно, итоговый результат fill in the required form fields")


def test_login_form_12(page: Page):
    my_string = ""
    # Цикл, который будет выполняться, пока длина строки меньше 70
    while len(my_string) < 70:
        my_string += "s"

    print("Протестируем поля на ограничение символов")
    page.goto("http://localhost:3000/")
    expect(page.locator(".login-form h2")).to_have_text("Login")
    print("Открылась форма")

    page.locator("#username").fill(my_string)
    print(f"Заполняем поле user-name очень длинным текстовым значением")

    page.locator("#password").fill(my_string)
    print(f"Заполняем поле password очень длинным текстовым значением")

    # получаем значения из полей
    input_user_value = page.input_value('#username')
    input_pass_value = page.input_value('#password')

    print("Проверяем ограничение полей на длину до 64 символов включительно")
    assert len(input_user_value) <= 64 and len(input_pass_value) <= 64
    print("Поля формы имеют ограничения в 64 символа, все ОК")


