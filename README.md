
## Projectjob_openings

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
## 🛠 Инструменты
<div align="center">
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192107858-fe19f043-c502-4009-8c47-476fc89718ad.png" alt="REST" title="REST"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192108372-f71d70ac-7ae6-4c0d-8395-51d8870c2ef0.png" alt="Git" title="Git"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png" alt="GitHub" title="GitHub"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" alt="Visual Studio Code" title="Visual Studio Code"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192109061-e138ca71-337c-4019-8d42-4792fdaa7128.png" alt="Postman" title="Postman"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" alt="Django" title="Django"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png" alt="MySQL" title="MySQL"/></code>
	<code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/136815194/82df4543-236b-4e45-9604-5434e3faab17" alt="SQLite" title="SQLite"/></code>
</div>

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
