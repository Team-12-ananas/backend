from django.db import models

choices_company = [
    ('company1', 'Компания 1'),
    ('company2', 'Компания 2'),
    ('company3', 'Зеленые человечки'),
]

industry_choices = [
        ('ux_designer', 'UX дизайнер'),
        ('python_developer', 'Python-разработчик'),
        ('project_manager', 'Project manager'),
        ('frontend_developer', 'Frontend/Web разработчик'),
        ('backend_developer', 'Backend разработчик'),
    ]
location_choices = [
        ('office', 'Офис'),
        ('remote', 'Удаленная работа'),
        ('hybrid', 'Гибридный график'),
    ]
employment_choices = [
        ('full_time', 'Полная занятость'),
        ('internship', 'Стажировка'),
        ('remote', 'Удаленная работа'),
        ('part_time', 'Частичная занятость'),
        ('temporary', 'Временная работа'),
        ('freelance', 'Подработка'),
    ]
education_choices = [
        ('higher', 'Высшее'),
        ('secondary', 'Среднее'),
        ('incomplete_higher', 'Неоконченное высшее'),
    ]


class Company(models.Model):
    """Модель компании HRa"""
    name_company = models.CharField(
        max_length=200,
        choices=choices_company,
    )

    class Meta:
        ordering = ('name_company',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name_company


class Hardskils(models.Model):
    """Модель хард скилов"""
    name = models.CharField(
        'Название Тега',
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой хард скил уже есть в бд',
        },
    )
    slug = models.SlugField(
        'Уникальный Тег',
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        },
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель вакансии"""
    dateIns = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
        )
    employer = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company',
        verbose_name='Автор вакансии',
    )
    name = models.CharField(
        'название вакансии',
        max_length=150,
        choices=industry_choices
    )
    description = models.TextField(
        'описание вакансии',
        help_text='напишите о вакансии'
        )
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    specialty = models.ManyToManyField(
        Hardskils,
        verbose_name='Харды',
    )
    education = models.CharField(
        'Образование',
        max_length=100,
        choices=education_choices
    )
    location = models.CharField(
        'Вид работы',
        max_length=150,
        choices=location_choices
    )
    employmentType = models.CharField(
        'Вид занятости',
        max_length=120,
        choices=employment_choices
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(
        'Город',
        max_length=120,
    )

    class Meta:
        ordering = ('dateIns',)
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name
