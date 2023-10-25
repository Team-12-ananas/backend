from django.db import models

from app_hr.validate import validate_username


class Company(models.Model):
    """Модель компании HRa"""
    name_company = models.CharField(
        validators=(validate_username,),
        max_length=120,
        unique=True,
        error_messages={
            'unique': 'Такая компания существует',
        },
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
        max_length=100
    )
    employmentType = models.CharField(
        'Вид занятости',
        max_length=120
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(
        'Город',
        max_length=120,
    )
