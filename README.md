# django_orm

Это учебный проект на Django, демонстрирующий работу с ORM через приложение `company`. В проекте реализованы модели для хранения данных организации: филиалы, отделы и сотрудники, а также примеры запросов для работы с базой данных.

## Описание
### Структура проекта
```
django_orm/
├── .github/
│   └── workflows/
│       ├── ruff.yml          # GitHub Actions: проверка кода через ruff
│       └── test.yml          # GitHub Actions: запуск Django-тестов
├── company/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Модели: Branch, Department, Employee
│   ├── tests.py
│   └── views.py
├── django_orm/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .ruff_cache/              # Кэш, генерируемый инструментом ruff
├── .venv/                    # Виртуальное окружение Python (локально)
├── db.sqlite3
├── manage.py
├── pyproject.toml            # Конфигурация ruff
├── requirements.in           # Зависимости проекта (pip-tools)
├── requirements.txt          # Сгенерированный файл зависимостей
└── README.md
```

Проект включает следующие модели:

- **Branch (Филиал):**
  - `name`: Короткое название филиала.
  - `address`: Адрес филиала.

- **Department (Отдел):**
  - `name`: Название отдела.
  - `floor`: Этаж, на котором расположен отдел.
  - `branch`: Связь с филиалом (при удалении филиала поле становится `NULL`).

- **Employee (Сотрудник):**
  - `first_name` и `last_name`: Имя и фамилия сотрудника.
  - `position`: Должность (обязательное поле).
  - `phone_number`: Номер телефона.
  - `birth_date`: Дата рождения.
  - `email`: Email сотрудника.
  - `department`: Связь с отделом (при удалении отдела сотрудник удаляется каскадно).

## Особенности проекта

- **Модели и связи:** Созданы модели с необходимыми полями и связями между ними (ForeignKey).
- **Миграции:** Реализована работа с миграциями для синхронизации моделей с базой данных.
- **Примеры запросов:** Проект включает примеры ORM-запросов, таких как:
  - Подсчет сотрудников с должностью "Менеджер".
  - Получение списка сотрудников, работающих на определённых этажах.
  - Фильтрация сотрудников по филиалам с использованием Q-объектов и оператора `__in`.
  - Получение ФИО сотрудников без email.
  - Фильтрация сотрудников по году рождения (например, 1990).

## Установка и запуск
###
1. **Клонируйте репозиторий:**
   ```
   git clone <URL_репозитория>
   cd django_orm
   ```
2. **Создайте и активируйте виртуальное окружение:**
   ```
	python3 -m venv venv
	source venv/bin/activate
   ```
3. **Установите зависимости:**
   ```
	pip install -r requirements.txt
   ```
	Если файла requirements.txt нет, установите необходимые пакеты вручную:
   ```
	pip install django ipython
   ```
4. **Настройка переменных окружения: При необходимости создайте файл .env и укажите нужные переменные.**
5. **Выполните миграции:**
   ```
	./manage.py makemigrations
	./manage.py migrate
	```
6. **Заполните базу данных тестовыми данными: Запустите Django shell:**
   ```
	./manage.py shell
	```
	и выполните команды для создания объектов моделей (филиалов, отделов, сотрудников).

	#### Создание Филиалов
	Начнем с добавления нескольких филиалов. Например, три филиала с разными адресами и названиями.
	```
	branch1 = Branch.objects.create(name="На 1905 года", address="Москва, ул. 1905 года, д. 7, строение 1")
	branch2 = Branch.objects.create(name="На Тверской", address="Москва, Тверская ул., д. 3")
	branch3 = Branch.objects.create(name="На Арбат", address="Москва, Арбат ул., д. 10")
	```
	#### Создание Отделов
	Добавим несколько отделов для каждого филиала.
	```
	department1 = Department.objects.create(name="Отдел маркетинга", floor=4, branch=branch1)
	department2 = Department.objects.create(name="Технический отдел", floor=5, branch=branch1)
	department3 = Department.objects.create(name="Отдел продаж", floor=2, branch=branch2)
	department4 = Department.objects.create(name="Юридический отдел", floor=3, branch=branch2)
	department5 = Department.objects.create(name="Отдел кадров", floor=6, branch=branch3)
	```
	#### Создание Сотрудников
	Теперь давайте добавим несколько сотрудников в каждый из отделов. Обратите внимание, что для каждого сотрудника нужно указать department (отдел).
	```
	employee1 = Employee.objects.create(first_name="Иван", last_name="Иванов", position="Менеджер", birth_date="1990-05-15", email="", department=department1)
	employee2 = Employee.objects.create(first_name="Мария", last_name="Петрова", position="Инженер", birth_date="1985-03-20", email="", department=department2)
	employee3 = Employee.objects.create(first_name="Алексей", last_name="Смирнов", position="Менеджер", birth_date="1992-08-10", email="smirnov@example.com", department=department3)
	employee4 = Employee.objects.create(first_name="Анна", last_name="Кузнецова", position="Юрист", birth_date="1990-12-25", email="kuznetsova@example.com", department=department4)
	employee5 = Employee.objects.create(first_name="Дмитрий", last_name="Васильев", position="Менеджер", birth_date="1994-11-30", email="vasilyev@example.com", department=department5)
	```
	#### Проверка и Отображение Записей
	Теперь вы можете проверить, что данные добавлены в базу:
	```
	# Проверка филиалов
	Branch.objects.all()

	# Проверка отделов
	Department.objects.all()

	# Проверка сотрудников
	Employee.objects.all()
	```
	После этого, у вас будут три филиала, пять отделов и пять сотрудников, распределённых по этим отделам.

## Запросы:

1. **Получить количество сотрудников с должностью "Менеджер":**

   ```python
   manager_count = Employee.objects.filter(position="Менеджер").count()
   ```

2. **Получить список сотрудников, работающих на четвертых этажах:**

   ```python
   employees_fourth_floor = Employee.objects.filter(department__floor=4)
   ```

3. **Получить список всех сотрудников, работающих в двух выбранных филиалах (с использованием Q):**

   ```python
   from django.db.models import Q

   # Предполагается, что branch1 и branch2 — это два выбранных филиала.
   employees_in_two_branches = Employee.objects.filter(
       Q(department__branch__id=branch1.id) | Q(department__branch__id=branch2.id)
   )
   ```

4. **Получить список сотрудников, работающих в тех же двух филиалах (с использованием lookup __in):**

   ```python
   employees_in_two_branches_lookup = Employee.objects.filter(
       department__branch__id__in=[branch1.id, branch2.id]
   )
   ```

5. **Получить список ФИО сотрудников, у которых не указан email:**

   ```python
   from django.db.models import Q, Value
   from django.db.models.functions import Concat

   employees_without_email = Employee.objects.filter(
       Q(email__isnull=True) | Q(email='')
   ).annotate(
       full_name=Concat('first_name', Value(' '), 'last_name')
   ).values_list('full_name', flat=True)
   ```

6. **Получить список сотрудников, чей год рождения 1990:**

   ```python
   employees_born_1990 = Employee.objects.filter(birth_date__year=1990)
   ```
## Лицензия
Этот проект распространяется под лицензией MIT License.
