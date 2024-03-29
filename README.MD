# Блог API

Этот проект представляет собой простое API для управления постами в блоге, разработанное с использованием Django и Django REST Framework.

## Установка

Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Wandering-npc/blog-api.git
```

2. Перейдите в директорию проекта:

```bash
cd blog-api
```

3. Создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Примените миграции:

```bash
python manage.py migrate
```

6. Создайте суперюзера:

```bash
python manage.py createsuperuser
```
7. Запустите сервер:

```bash
python manage.py runserver
```

## Использование
У проекта имеется OpenApi документация. Она доступна по адресам `api/redoc/` или `api/swagger/`

### Создание поста

Вы можете создать новый пост, отправив POST запрос на `/api/posts/` с данными о посте в формате JSON.

Пример запроса:

```json
{
  "title": "Новый пост",
  "text": "Текст нового поста",
  "published": true
}
```

### Получение списка постов

Чтобы получить список всех постов, отправьте GET запрос на `/api/posts/`.

### Работа с одним постом

Для просмотра, редактирования, удаления поста направье соответсвующий запрос на `/api/posts/{post_id}/`, где `{post_id}` - идентификатор поста.

## Тестирование

Для запуска тестов используйте команду:

```bash
python manage.py test
```

update

