from django.db import models

# Create your models here.
class VHD(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Код вида хозяйственной деятельности")
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Наименование")

    def __str__(self):
        return f"{self.id}, {self.name}"

    class Meta:
        verbose_name_plural = "Виды хозяйственной деятельности"


class FO(models.Model):
    Name_choices = [
        ('ТОО', 'Товарищество с ограниченной ответственностью'),
        ('ИП', 'Индивидуальный предприниматель'),
        ('ООО', 'Общество с ограниченной ответственностью'),
        ('АО', 'Акционерное общество'),
        ('ЗАО', 'Закрытое акционерное общество'),
    ]
    id = models.AutoField(primary_key=True, verbose_name="Код")
    name = models.CharField(max_length=50, choices=Name_choices, verbose_name="Наименование")

    def __str__(self):
        return f"{self.id}, {self.name}"

    class Meta:
        verbose_name_plural = "Формы организации"


class NK(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Код комитета")
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Наименование")
    address = models.CharField(max_length=60, blank=False, unique=True, verbose_name="Адрес")

    def __str__(self):
        return f"{self.id}, {self.name}"

    class Meta:
        verbose_name_plural = "Налоговые комитеты"


class Bank(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Код банка")
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Наименование")
    address = models.CharField(max_length=60, blank=False, unique=True, verbose_name="Адрес")

    def __str__(self):
        return f"{self.id}, {self.name}"

    class Meta:
        verbose_name_plural = "Банки"


class Predpriyatie(models.Model):
    bin_id = models.CharField(primary_key=True, max_length=12, unique=True, blank=False, verbose_name="БИН")
    full_name = models.CharField(max_length=100, blank=False, unique=True, verbose_name="Полное наименование")
    sh_name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Сокращенное наименование")
    address = models.CharField(max_length=60, blank=False, unique=True, verbose_name="Адрес")
    phone = models.CharField(max_length=11, unique=True, blank=False, verbose_name="Телефон")
    fio_ruk = models.CharField(max_length=50, blank=False, unique=True, verbose_name="ФИО руководителя")
    form_org = models.ForeignKey(FO, on_delete=models.CASCADE, verbose_name="Код формы организации")
    vid_hoz_d = models.ForeignKey(VHD, on_delete=models.CASCADE,
                                  verbose_name="Код основного вида хозяйственной деятельности")
    date = models.DateField(verbose_name="Дата постановки на учет")
    nalog_kom = models.ForeignKey(NK, on_delete=models.CASCADE, verbose_name="Код налогового комитета")
    chislo_rab = models.PositiveIntegerField(verbose_name="Число работников")
    uchrediteli = models.CharField(max_length=200, unique=True, verbose_name="Учредители")

    def __str__(self):
        return f"{self.bin_id}, {self.full_name}"

    class Meta:
        verbose_name_plural = "Предприятия"


class PB(models.Model):
    bin_pb = models.ForeignKey(Predpriyatie, on_delete=models.CASCADE, verbose_name="БИН", related_name='predpriyatie')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="Код банка")
    schet = models.CharField(max_length=20, unique=True, blank=False, verbose_name="Лицевой счет")

    def __str__(self):
        return f"{self.bin_pb},{self.schet}"

    class Meta:
        verbose_name_plural = "Предприятия_банки"


class PVD(models.Model):
    bin_pvd = models.ForeignKey(Predpriyatie, on_delete=models.CASCADE, verbose_name="БИН")
    vid_hoz_d = models.ForeignKey(VHD, on_delete=models.CASCADE, verbose_name="Код вида хозяйственной деятельности")

    class Meta:
        verbose_name_plural = "Предприятия_виды деятельности"


class BS(models.Model):
    kod = models.CharField(max_length=4, primary_key=True, unique=True, verbose_name="Код счета")
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Наименование")

    def __str__(self):
        return f"{self.kod}, {self.name}"

    class Meta:
        verbose_name_plural = "Бухгалтерские счета"


class FP(models.Model):
    priznaki = [
        ('Дебет', 'Дт'),
        ('Кредит', 'Кт'),

    ]
    kv_choices = [
        ('Первый', '1'),
        ('Второй', '2'),
        ('Третий', '3'),
        ('Четвертый', '4'),
    ]
    bin_fp = models.ForeignKey(Predpriyatie, on_delete=models.CASCADE, verbose_name="БИН")
    kvartal = models.CharField(max_length=50, choices=kv_choices, verbose_name="Квартал")
    date = models.IntegerField(verbose_name="Год")
    bs = models.ForeignKey(BS, on_delete=models.CASCADE, verbose_name="Код счета")
    summa = models.PositiveIntegerField(verbose_name="Сумма")
    priznak = models.CharField(max_length=50, choices=priznaki, verbose_name="Признак")

    def __str__(self):
        return f"{self.bin_fp}"

    class Meta:
        verbose_name_plural = "Финансовые показатели"
