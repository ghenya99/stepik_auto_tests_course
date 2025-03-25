from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    btn = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)


    btn.click()

finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

