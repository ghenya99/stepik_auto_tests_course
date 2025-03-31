from selenium.webdriver.common.by import By
import time

def test_item_has_add_to_basket_button(browser):

    # Arrange
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Act
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    # Assert
    assert add_to_basket_button, "Add to basket button not found"
    time.sleep(30)