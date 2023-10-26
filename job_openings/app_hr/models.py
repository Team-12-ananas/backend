from django.db import models


class Location(models.Model):
    """Вид деятельности"""
    name_location = models.CharField(
        'Вид работы',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такая деятельность уже есть',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг вида образования",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('name_location',)
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'

    def __str__(self):
        return self.name_location


class Education(models.Model):
    """Модель образования"""
    name_education = models.CharField(
        'Образование',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такой вид образования есть в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг вида образования",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('name_education',)
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

    def __str__(self):
        return self.name_education


class Employment(models.Model):
    "Модель тега занятости"
    name_employment = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой вид работы есть в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг вида работы",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('name_employment',)
        verbose_name = 'Тег занятости'
        verbose_name_plural = 'Теги занятости'

    def __str__(self):
        return self.name_employment


class Company(models.Model):
    """Модель компании HRa"""
    name_company = models.CharField(
        max_length=200,
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
    education = models.ForeignKey(
        Education,
        verbose_name='Образование',
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Вид работы',
        on_delete=models.CASCADE,
    )
    employmentType = models.ForeignKey(
        Employment,
        verbose_name='Тип работы',
        on_delete=models.CASCADE,
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
