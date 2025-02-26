from django.urls import path, include

from django.urls import get_resolver

# Вывод всех маршрутов при запуске сервера
#for pattern in get_resolver().url_patterns:
#    print(pattern)

urlpatterns = [
    path("api/users/", include("users.urls")),
]
