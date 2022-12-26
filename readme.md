# Реализовано:

- Основной функционал
- Тестирование
- Докер сборка
- Swagger схема
- Обработка ошибок при ненадежности стороннего API

# Запуск проекта

- Клонировать в локальный репозиторий

# Без makefile:

- $ docker build ./mailing -t mailing_app
- docker-compose up -d

# С makefile:

- $ make build
- $ make run

# Тестирование:

- $ Запустить контейнеры (должен работать Celery)
- $ make test
  или
- $ docker-compose run --rm app python -m pytest
