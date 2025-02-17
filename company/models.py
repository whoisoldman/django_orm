from django.db import models

# Модель для филиала
class Branch(models.Model):
    name = models.CharField(max_length=255)  # Короткое название филиала
    address = models.CharField(max_length=255)  # Адрес филиала

    def __str__(self):
        return self.name

# Модель для отдела
class Department(models.Model):
    name = models.CharField(max_length=255)  # Название отдела
    floor = models.IntegerField()  # Этаж, на котором расположен отдел
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)  # Связь с филиалом

    def __str__(self):
        return self.name

# Модель для сотрудника
class Employee(models.Model):
    first_name = models.CharField(max_length=100)  # Имя
    last_name = models.CharField(max_length=100)  # Фамилия
    position = models.CharField(max_length=255)  # Должность
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона
    birth_date = models.DateField()  # Дата рождения
    email = models.EmailField(blank=True, null=True)  # Email
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Связь с отделом

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
