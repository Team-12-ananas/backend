
## Todo projectjob_openings

Проект написан для реализации приложения по поиску работы.

примеры GET запроса к бд: 
- Все вакансии http://127.0.0.1:8000/api/vacancy/
```
[
    {
        "dateIns": "2023-10-27T13:23:35.813522Z",
        "city": "Санкт Петербург",
        "description": "Не придумал",
        "email": "varlamy4@ya.ru",
        "min_salary": 1000,
        "max_salary": 125000,
        "name": "Gastrobar Moro",
        "phone": "+79990228292",
        "author_vacancy": "Самая лучшая",
        "education": "Среднее",
        "employmentType": [
            "Гибрид",
            "Офис"
        ],
        "jobexpiriense": "Полная занятость",
        "projectActivities": "Самое лучшее",
        "specializationType": "Ract",
        "specialty": "Front develop",
        "keyskils": [
            "16 часов на ногах"
        ],
        "active_vacancy": true
    }
]
```
- Все компании http://127.0.0.1:8000/api/company/
```
[
    {
        "name_company": "Самая лучшая"
    }
]
```
- Все вакансии одной компании http://127.0.0.1:8000/api/company/1
```
{
    "company": {
        "name_company": "Самая лучшая"
    },
    "vacancies": [
        {
            "dateIns": "2023-10-27T13:23:35.813522Z",
            "city": "Санкт Петербург",
            "description": "Не придумал",
            "email": "varlamy4@ya.ru",
            "min_salary": 1000,
            "max_salary": 125000,
            "name": "Gastrobar Moro",
            "phone": "+79990228292",
            "author_vacancy": "Самая лучшая",
            "education": "Среднее",
            "employmentType": [
                "Гибрид",
                "Офис"
            ],
            "jobexpiriense": "Полная занятость",
            "projectActivities": "Самое лучшее",
            "specializationType": "Ract",
            "specialty": "Front develop",
            "keyskils": [
                "16 часов на ногах"
            ],
            "active_vacancy": true
        }
    ]
}
```

### Для установки проекта
- Cклонировать проект команндой 
```
git@github.com:Team-12-ananas/backend.git
```
- Установить вертульное окружение
```
python -m venv venv
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Установить миграции
```
python manage.py migrate
```
- Запустить проект
```
python manage.py runserver
```

## Authors
Варламов Н.О.
- [@Devarlamov](https://www.github.com/devarlamov)