from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Селекторы для элементов на странице
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    USER_INFO_SECTION = (By.ID, "userInfo")
    LOGOUT_BUTTON = (By.ID, "logoutButton")
    USER_NAME_SPAN = (By.ID, "userName")

    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        """Открывает страницу логина"""
        self.driver.get(url)

    def enter_username(self, username):
        """Вводит имя пользователя"""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """Вводит пароль"""
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Нажимает кнопку входа"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Выполняет полный процесс входа"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        """Выполняет выход из системы"""
        try:
            self.driver.find_element(*self.LOGOUT_BUTTON).click()
            # Ждем, пока форма логина снова появится
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.USERNAME_INPUT)
            )
        except:
            pass

    def wait_for_page_load(self):
        """Ожидает загрузки страницы"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )

    def wait_for_success_message(self, timeout=10):
        """Ожидает появления сообщения об успехе"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            return True
        except:
            return False

    def wait_for_error_message(self, timeout=10):
        """Ожидает появления сообщений об ошибках"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located(self.ERROR_MESSAGE)
            )
            return True
        except:
            return False

    def wait_for_user_info(self, timeout=10):
        """Ожидает появления информации о пользователе"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.USER_INFO_SECTION)
            )
            return True
        except:
            return False

    def is_login_form_displayed(self):
        """Проверяет, отображается ли форма логина"""
        try:
            return self.driver.find_element(*self.USERNAME_INPUT).is_displayed()
        except:
            return False

    def get_user_name(self):
        """Возвращает имя вошедшего пользователя"""
        try:
            element = self.driver.find_element(*self.USER_NAME_SPAN)
            return element.text
        except:
            return None

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке"""
        try:
            # Ищем все error messages
            error_elements = self.driver.find_elements(*self.ERROR_MESSAGE)
            for element in error_elements:
                if element.is_displayed():
                    return element.text
            return None
        except:
            return None
