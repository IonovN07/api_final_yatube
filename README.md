# Yatube API
## Описание
Yatube API — это интерфейс для взаимодействия с платформой Yatube.

#### С помощью Yatube API пользователи могут:

- создавать и публиковать собственные посты;
- редактировать и удалять свои посты;
- оставлять комментарии под публикациями других авторов;
- подписываться на интересующих авторов.

Yatube API предоставляет удобный и гибкий способ взаимодействия с платформой Yatube для разработчиков и пользователей.

## Как запустить проект:
#### Клонировать репозиторий и перейти в него в командной строке:
```git clone git@github.com:IonovN07/api_final_yatube.git```

```cd api_final_yatube```
#### Cоздать и активировать виртуальное окружение:
```python3 -m venv env```

```source env/bin/activate```

```python3 -m pip install --upgrade pip```
#### Установить зависимости из файла requirements.txt:
```pip install -r requirements.txt```
#### Выполнить миграции:
```python3 manage.py migrate```
#### Запустить проект:
```python3 manage.py runserver```

## Примеры запросов:
### Получение списка всех постов
| Метод | GET |
| --- | --- |
| URL | http://127.0.0.1:8000/api/v1/posts/ |
#### Ответ:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
} 
```

### Добавление нового поста
| Метод: | POST |
| --- | --- |
| URL: | http://127.0.0.1:8000/api/v1/posts/ |

#### Тело запроса:
```json
{
   "text": "string",
   "image": "string",
   "group": 0
}
```
#### Ответ:
```json
{
   "id": 0,
   "author": "string",
   "text": "string",
   "pub_date": "2025-05-14T14:15:22Z",
   "image": "string",
   "group": 0
}
```

#### Описание эндпоинтов с примерами доступно по адресу: http://127.0.0.1:8000/redoc/
