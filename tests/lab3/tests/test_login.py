from login_page import LoginPage
from constants import VALID_CREDENTIALS, INVALID_CREDENTIALS, INVALID_CREDENTIALS_WITH_EMPTY_FIELDS


class TestLogin:
    def test_all_valid_credentials(self, driver, login_page_url):
        """Тест входа со всеми валидными комбинациями"""
        login_page = LoginPage(driver)

        for username, password in VALID_CREDENTIALS:
            login_page.load(login_page_url)
            login_page.wait_for_page_load()

            login_page.login(username, password)
            if not login_page.wait_for_success_message(10):
                raise AssertionError(
                    "Login was not successful - success message not displayed")

            if not login_page.wait_for_user_info(10):
                raise AssertionError(
                    "Login was not successful - user info not displayed")

            # Дополнительная проверка: имя пользователя отображается корректно
            displayed_name = login_page.get_user_name()
            assert displayed_name == username, f"Expected {username}, got {displayed_name}"

    def test_all_invalid_credentials(self, driver, login_page_url):
        """Тест входа со всеми невалидными комбинациями"""
        login_page = LoginPage(driver)

        for username, password in INVALID_CREDENTIALS:
            login_page.load(login_page_url)
            login_page.wait_for_page_load()

            login_page.login(username, password)
            if not login_page.wait_for_error_message(10):
                raise AssertionError(
                    "Error message did not appear for invalid credentials")

            # Дополнительная проверка: ошибка отображается корректно
            error_text = login_page.get_error_message()
            assert "Неверное имя пользователя или пароль" in error_text or "error" in error_text.lower(), \
                f"Unexpected error message: {error_text}"

    def test_login_with_empty_fields(self, driver, login_page_url):
        """Тест входа с пустыми полями"""
        login_page = LoginPage(driver)

        for username, password in INVALID_CREDENTIALS_WITH_EMPTY_FIELDS:
            login_page.load(login_page_url)
            login_page.wait_for_page_load()

            login_page.login(username, password)
            if not login_page.wait_for_error_message(10):
                raise AssertionError(
                    "Error message did not appear for invalid credentials")

            # Проверяем, что остались на странице логина
            assert login_page.is_login_form_displayed(), \
                "Should stay on login page with empty fields"

    def test_logout_functionality(self, driver, login_page_url):
        """Тест функциональности выхода"""
        login_page = LoginPage(driver)
        login_page.load(login_page_url)
        login_page.wait_for_page_load()

        # Логинимся
        username, password = VALID_CREDENTIALS[0]
        login_page.login(username, password)

        # Ждем успешного входа
        login_page.wait_for_success_message(10)

        # Ждем перехода к user info
        login_page.wait_for_user_info(10)

        # Выполняем выход
        login_page.logout()

        # Проверяем, что вернулись к форме логина
        assert login_page.is_login_form_displayed(), \
            "Should return to login form after logout"

    def test_ui_elements_presence(self, driver, login_page_url):
        """Тест наличия всех UI элементов"""
        login_page = LoginPage(driver)
        login_page.load(login_page_url)
        login_page.wait_for_page_load()

        # Проверяем наличие основных элементов
        assert login_page.is_login_form_displayed(), "Login form should be displayed"
        assert driver.find_element(
            *login_page.USERNAME_INPUT).is_displayed(), "Username input should be visible"
        assert driver.find_element(
            *login_page.PASSWORD_INPUT).is_displayed(), "Password input should be visible"
        assert driver.find_element(
            *login_page.LOGIN_BUTTON).is_displayed(), "Login button should be visible"
        assert driver.find_element(
            *login_page.LOGIN_BUTTON).is_enabled(), "Login button should be enabled"
