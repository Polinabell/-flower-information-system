# Microservices with Docker and Docker Compose

Этот проект демонстрирует два микросервиса, которые общаются друг с другом через Docker Compose.

## Структура проекта

- `service1/` - Первый микросервис (порт 5000)
- `service2/` - Второй микросервис (порт 5001)
- `docker-compose.yml` - Конфигурация Docker Compose

## Запуск проекта

1. Убедитесь, что у вас установлены Docker и Docker Compose
2. Клонируйте репозиторий
3. Выполните команду:
   ```bash
   docker-compose up --build