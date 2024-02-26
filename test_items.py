import time
from selenium.webdriver.common.by import By


class TestProductDetails:

    def test_check_add_to_basket_button_visibility(self, browser):
        """Проверка видимости кнопки 'Добавить в корзину' на странице товара"""

        # Открытие страницы товара
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.maximize_window()  # Максимизация окна браузера

        # Временная задержка для визуальной проверки языка открытой страницы
        time.sleep(2)

        # Проверка наличия кнопки добавления товара в корзину с использованием XPath
        assert browser.find_element(By.XPATH, '//form[@id="add_to_basket_form"]//button')
