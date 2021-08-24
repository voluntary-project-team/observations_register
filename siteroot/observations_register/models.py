from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = (('М', 'Мужской'), ('Ж', 'Женский'))
    EYES_CHOICES = (('ГОЛУБОЙ', 'Голубой'), ('СЕРЫЙ', 'Серый'),
                    ('ЗЕЛЕНЫЙ', 'Зеленый'), ('КАРИЙ', 'Карий'))
    HAIR_CHOICES = (('БЛОНДИН', 'Блондин'), ('РЫЖИЙ', 'Рыжий'),
                    ('ТЕМНЫЙ', 'Темный'), ('ЧЕРНЫЙ', 'Черный'))

    fullname = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    eyes_col = models.CharField(max_length=7, choices=EYES_CHOICES)
    hair_col = models.CharField(max_length=7, choices=HAIR_CHOICES)

    def __str__(self):
        return self.fullname

    def get_questionnaires(self):
        if not hasattr(self, '_questionnaires'):
            self._questionnaires = self.questionnaire_set.all()
        return self._questionnaires


class Questionnaire(models.Model):
    FRECKLES_CHOICES = (('МНОГО', 'Много'), ('УМЕРЕННО', 'Умеренно'),
                        ('ЕДИНИЧНЫЕ', 'Единичные'), ('НЕТ', 'Нет'))
    SKIN_CHOICES = (('ОЧЕНЬ БЕЛЫЙ', 'Очень белый'), ('БЕЛЫЙ', 'Белый'),
                    ('СВЕТЛО-БЕЖЕВЫЙ', 'Светло-бежевый'), ('КОРИЧНЕВЫЙ', 'Коричневый'),
                    ('ТЕМНО-КОРИЧНЕВЫЙ', 'Темно-коричневый'))
    TANNING_CHOICES = (('СИЛЬНО СГОРАЕТ', 'Сильно сгорает'), ('УМЕРЕННО СГОРАЕТ', 'Умеренно сгорает'),
                       ('ИНОГДА СГОРАЕТ', 'Иногда сгорает'), ('СГОРАЕТ РЕДКО', 'Сгорает редко'),
                       ('НЕ СГОРАЕТ', 'Не сгорает'))
    REST_CHOICES = (('10 ДНЕЙ В ГОД', '10 дней в год'), ('20 ДНЕЙ В ГОД', '20 дней в год'),
                    ('БОЛЬШЕ 20 ДНЕЙ В ГОД', 'Больше 20 дней в год'),
                    ('НЕ ОТДЫХАЮ НА ЮГЕ', 'Не отдыхаю на юге'))
    NEO_APPEAR_CHOICES = (('ПОМНЮ С ДЕТСТВА', 'Помню с детства'), ('НЕДАВНО', 'Недавно'),
                          ('НЕ МОГУ ОТВЕТИТЬ','Не могу ответить'))
    NEO_LOC_CHOICES = (('ВОЛОСИСТАЯ ЧАСТЬ ГОЛОВЫ', 'Волосистая часть головы'), ('ЛИЦО', 'Лицо'),
                       ('ШЕЯ','Шея'), ('ДЕКОЛЬТЕ', 'Декольте'),
                       ('ПЛЕЧО', 'Плечо'), ('ПРЕДПЛЕЧЬЕ', 'Предплечье'),
                       ('КИСТЬ', 'Кисть'), ('НИЖНЯЯ ЧАСТЬ ТУЛОВИЩА', 'Нижняя часть туловища'),
                       ('БЕДРО', 'Бедро'), ('ГОЛЕНЬ', 'Голень'), ('СТОПА', 'Стопа'))
    ELEM_BORDERS_CHOICES = (('ЧЕТКИЕ', 'Четкие'), ('НЕЧЕТКИЕ', 'Нечеткие'))
    ELEM_COLOR_CHOICES = (('КРАСНЫЙ', 'Красный'), ('БЕЖЕВЫЙ', 'Бежевый'),
                          ('КОРИЧНЕВЫЙ', 'Коричневый'), ('ЧЕРНЫЙ', 'Черный'))

    #fields are required
    date_of_visit = models.DateField(auto_now=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    growth = models.PositiveSmallIntegerField()
    freckles = models.CharField(max_length=9, choices=FRECKLES_CHOICES)
    skin_col = models.CharField(max_length=16, choices=SKIN_CHOICES)
    redness_during_sunburn = models.BooleanField()
    tanning_character = models.CharField(max_length=16, choices=TANNING_CHOICES)
    rest_in_south = models.CharField(max_length=20, choices=REST_CHOICES)
    sunscreen_using = models.BooleanField()
    neoplasm_appearance = models.CharField(max_length=16, choices=NEO_APPEAR_CHOICES)
    neoplasm_location = models.CharField(max_length=23, choices=NEO_LOC_CHOICES)
    skin_tumors_in_fam = models.BooleanField()

    #fields are optional
    elem_size = models.PositiveSmallIntegerField(null=True, blank=True)
    elem_area = models.PositiveSmallIntegerField(null=True, blank=True)
    elem_borders = models.CharField(max_length=8, choices=ELEM_BORDERS_CHOICES, null=True, blank=True)
    elem_color = models.CharField(max_length=10, choices=ELEM_COLOR_CHOICES, null=True, blank=True)
    inclusions = models.BooleanField(null=True)
    elem_symmetry = models.BooleanField(null=True)

    def __str__(self):
        return self.patient.fullname + " " + str(self.date_of_visit)

