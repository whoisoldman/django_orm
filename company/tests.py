"""Тесты для моделей приложения компании."""

from datetime import date

from django.test import TestCase

from .models import Branch, Department, Employee


class BranchModelTest(TestCase):
    """Тесты модели Branch."""

    def setUp(self):
        """Настройка данных для теста филиала."""
        Branch.objects.create(name="Main Branch")

    def test_branch_name(self):
        """Тестирование имени филиала."""
        branch = Branch.objects.get(name="Main Branch")
        self.assertEqual(branch.name, "Main Branch")

class DepartmentModelTest(TestCase):
    """Тесты модели Department."""

    def setUp(self):
        """Настройка данных для теста отдела."""
        branch = Branch.objects.create(name="Main Branch")
        Department.objects.create(name="HR", branch=branch, floor=1)

    def test_department_name(self):
        """Тестирование имени отдела."""
        department = Department.objects.get(name="HR")
        self.assertEqual(department.name, "HR")

class EmployeeModelTest(TestCase):
    """Тесты модели Employee."""

    def setUp(self):
        """Настройка данных для теста сотрудника."""
        branch = Branch.objects.create(name="Main Branch")
        department = Department.objects.create(name="HR", branch=branch, floor=1)
        Employee.objects.create(
            first_name="John",
            last_name="Doe",
            department=department,
            birth_date=date(1990, 1, 1)
        )

    def test_employee_full_name(self):
        """Тестирование полного имени сотрудника."""
        employee = Employee.objects.get(first_name="John")
        full_name = f"{employee.first_name} {employee.last_name}"
        self.assertEqual(full_name, "John Doe")
