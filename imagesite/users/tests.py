import requests

BASE_URL = "http://127.0.0.1:8000/api/users/"

# Регистрация
register_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "Test@1234",
    "password2": "Test@1234"
}
response = requests.post(BASE_URL + "register/", json=register_data)
print("Регистрация:", response.json())

# Авторизация
login_data = {
    "email": "test@example.com",
    "password": "Test@1234"
}
response = requests.post(BASE_URL + "login/", json=login_data)
tokens = response.json()
print("Токены:", tokens)

# Доступ к защищённому маршруту
headers = {
    "Authorization": f"Bearer {tokens['access']}"
}
response = requests.get(BASE_URL + "protected/", headers=headers)
print("Защищённый маршрут:", response.json())
