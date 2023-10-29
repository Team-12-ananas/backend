from django.db import models


class Specialty(models.Model):
    """Модель специальности"""
    specialty = models.CharField(
        'Образование',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такая специальность в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг типа занятостия",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('specialty',)
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'

    def __str__(self):
        return self.specialty


class SpecializationType(models.Model):
    """Модель специализации"""
    specializationType = models.CharField(
        'Образование',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такая специализациия есть в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг типа занятостия",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('specializationType',)
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'

    def __str__(self):
        return self.specializationType


class ProjectActivities(models.Model):
    """Модель проетной активности"""
    projectActivities = models.CharField(
        'Образование',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такая проетной активности есть в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг типа занятостия",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('projectActivities',)
        verbose_name = 'проетной активность'
        verbose_name_plural = 'проетной активности'

    def __str__(self):
        return self.projectActivities


class JobExpiriense(models.Model):
    """Модель типа занятости"""
    jobexpiriense = models.CharField(
        'Образование',
        max_length=130,
        unique=True,
        error_messages={
            'unique': 'такой типа занятости есть в бд',
        },
    )
    slug = models.SlugField(
        "Уникальный слаг типа занятостия",
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'такой slug уже есть',
        }
    )

    class Meta:
        ordering = ('jobexpiriense',)
        verbose_name = 'занятость'
        verbose_name_plural = 'занятости'

    def __str__(self):
        return self.jobexpiriense


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
        verbose_name = "Хард скил"
        verbose_name_plural = "Хард скилы"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель вакансии"""
    dateIns = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
        )
    author_vacancy = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancy',
        verbose_name='Автор вакансии',
    )
    city = models.CharField(
        'Город',
        max_length=120,
    )
    description = models.TextField(
        'описание вакансии',
        help_text='напишите о вакансии'
        )
    education = models.ForeignKey(
        Education,
        verbose_name='Образование',
        on_delete=models.CASCADE,
    )
    email = models.EmailField()
    employmentType = models.ManyToManyField(
        Employment,
        verbose_name='Тип занятости',
    )
    jobexpiriense = models.ForeignKey(
        JobExpiriense,
        on_delete=models.CASCADE,
        verbose_name='опыт работы',
    )
    keyskils = models.ManyToManyField(
        Hardskils,
        verbose_name='Харды',
    )
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    name = models.CharField(
        'название вакансии',
        max_length=150,
    )
    phone = models.CharField(max_length=20)
    projectActivities = models.ForeignKey(
        ProjectActivities,
        on_delete=models.CASCADE,
        verbose_name='проектная активность',
    )
    specializationType = models.ForeignKey(
        SpecializationType,
        on_delete=models.CASCADE,
        verbose_name='Тип специализации',
        )
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        verbose_name='Cпециальность',
    )
    active_vacancy = models.BooleanField(default=True)

    class Meta:
        ordering = ('dateIns',)
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name


class Archive(models.Model):
    """Модель архива"""
    name_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='Компания'
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, verbose_name='Вакансия'
    )

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name_company', 'vacancy'], name='unique_arhive'
            )
        ]

    def __str__(self):
        return f'{self.name_company.name_company} - {self.vacancy.id}'
