import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJSONPlaceholderAPI:

    def test_get_user(self):
        """Test GET /users/1"""
        response = requests.get(f"{BASE_URL}/users/1")

        # Проверка статус кода
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Проверка структуры JSON
        data = response.json()
        expected_keys = ['id', 'name', 'username', 'email',
                         'address', 'phone', 'website', 'company']
        assert all(
            key in data for key in expected_keys), f"Missing keys in response"

        # Проверка вложенной структуры
        assert 'address' in data
        assert all(key in data['address'] for key in [
                   'street', 'suite', 'city', 'zipcode', 'geo'])
        assert all(key in data['address']['geo'] for key in ['lat', 'lng'])

        # Проверка значений полей
        assert data['id'] == 1
        assert data['name'] == "Leanne Graham"
        assert data['username'] == "Bret"
        assert data['email'] == "Sincere@april.biz"

        # Проверка Content-Type
        assert 'application/json' in response.headers['Content-Type']

        # Проверка времени ответа
        assert response.elapsed.total_seconds() < 2, "Response time too long"

    def test_create_user(self):
        """Test POST /users"""
        user_data = {
            "name": "John Doe",
            "username": "johndoe",
            "email": "john.doe@example.com",
            "phone": "1-770-736-8031",
            "website": "johndoe.org"
        }

        response = requests.post(f"{BASE_URL}/users", json=user_data)

        # Проверка статус кода
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        # Проверка структуры JSON
        response_data = response.json()
        expected_keys = ['id', 'name', 'username', 'email', 'phone', 'website']
        assert all(key in response_data for key in expected_keys)

        # Проверка значений полей
        assert response_data['name'] == user_data['name']
        assert response_data['username'] == user_data['username']
        assert response_data['email'] == user_data['email']
        assert response_data['phone'] == user_data['phone']
        assert response_data['website'] == user_data['website']

        # JSONPlaceholder всегда возвращает id=11 для новых пользователей
        assert response_data['id'] == 11

    def test_update_user(self):
        """Test PUT /users/1"""
        user_data = {
            "id": 1,
            "name": "John Smith",
            "username": "johnsmith",
            "email": "john.smith@example.com",
            "phone": "1-770-736-8031",
            "website": "johnsmith.org"
        }

        response = requests.put(f"{BASE_URL}/users/1", json=user_data)

        # Проверка статус кода
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Проверка структуры JSON
        response_data = response.json()
        expected_keys = ['id', 'name', 'username', 'email', 'phone', 'website']
        assert all(key in response_data for key in expected_keys)

        # Проверка значений полей
        assert response_data['id'] == user_data['id']
        assert response_data['name'] == user_data['name']
        assert response_data['username'] == user_data['username']
        assert response_data['email'] == user_data['email']
        assert response_data['website'] == user_data['website']

        # Проверка что данные обновились
        assert response_data['name'] == "John Smith"
        assert response_data['username'] == "johnsmith"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
