from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100") # Ждем когда цена дома упадет до 100 баксов
)
button_book = browser.find_element(By.ID, "book")
button_book.click()

x1 = browser.find_element(By.ID, "input_value")
x = x1.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(3)

print(browser.switch_to.alert.text)

browser.quit()