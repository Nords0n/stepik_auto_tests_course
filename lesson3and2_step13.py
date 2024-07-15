import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker


class TestRegistration_test(unittest.TestCase):
    def test_lesson1and6_step11_reg1(self):
        fake = Faker()
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys(fake.first_name())
        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second'][@required]")
        input2.send_keys(fake.last_name())
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
        input3.send_keys(fake.ascii_free_email())
        # input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Input your phone:')]")
        # input4.send_keys(fake.phone_number())
        # button = browser.find_element(By.XPATH, "//button[@type='submit']")
        # button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text,'"Congratulations! You have successfully registered!"')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_lesson1and6_step11_reg2(self):
        fake = Faker()
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys(fake.first_name())
        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second'][@required]")
        input2.send_keys(fake.last_name())
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
        input3.send_keys(fake.ascii_free_email())
        time.sleep(5)
        # input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Input your phone:')]")
        # input4.send_keys(fake.phone_number())
        # button = browser.find_element(By.XPATH, "//button[@type='submit']")
        # button.click()

        # input1 = browser.find_element(By.CSS_SELECTOR, "input:required")
        # input1.send_keys(fake.first_name())
        # input2 = browser.find_element(By.XPATH, "//input[@class='form-control third'][@required]")
        # input2.send_keys(fake.ascii_free_email())
        # input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Input your address')]")
        # input3.send_keys(fake.last_name())
        # input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Input your phone:')]")
        # input4.send_keys(fake.phone_number())
        # button = browser.find_element(By.XPATH, "//button[@type='submit']")
        # button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text,'"Congratulations! You have successfully registered!"')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
