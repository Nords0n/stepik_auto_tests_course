import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)  # Устанавливаем неявное ожидание
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('links', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])

def test_entering_authorization(browser, links):
    browser.get("https://stepik.org")

    # Явное ожидание появления кнопки "Войти"
    enter_button = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'navbar__auth_login')]"))
    )
    enter_button.click()

    login_value = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    login_value.send_keys("slavashiman09@gmail.com")

    password_value = browser.find_element(By.NAME, "password")
    password_value.send_keys("V&xU4FtnW<Ff}(ms")

    # Явное ожидание появления кнопки "Войти"
    login_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'sign-form__btn')]"))
    )
    login_button.click()

    # Убедимся, что логин успешен, проверив наличие элемента, видимого только в залогиненном состоянии
    user_icon = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'navbar__profile-img')]"))
    )

    browser.get(links)

    quick_math = str(math.log(int(time.time())))
    browser.get(links)

    input_value = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']"))
    )
    input_value.send_keys(quick_math)

    button_value = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'submit-submission')]"))
    )
    button_value.click()

    try:
        # Проверка сообщения об успехе
        message_element = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'smart-hints__hint')]"))
        )
        message_text = message_element.text
        print(f"Message found: {message_text}")

        # Assert message content
        assert message_text == "Correct!", f"Expected 'Correct!', but got '{message_text}'"
        print("Success message found and verified.")
    except Exception as e:
        print(f"Error finding success message: {e}")
        raise