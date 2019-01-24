from budget.models import Project,Category,Expense
from django.test import TestCase

class TestModels(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            name='project 1',
            budget=20000
        )

    def test_project_assigned_slug_creation(self):
        self.assertEquals(self.project1.slug,'project-1')

    def test_project_budget_left(self):
        category1 = Category.objects.create(
            project = self.project1,
            name = 'development'

        )

        Expense.objects.create(

            project=self.project1,
            title = 'expense 1',
            amount = 5000,
            category = category1

        )

        Expense.objects.create(

            project=self.project1,
            title = 'expense 2',
            amount = 2000,
            category = category1

        )

        self.assertEquals(self.project1.budget_left,13000)

    def test_project_total_transactions(self):
        project2 = Project.objects.create(
            name='project 2',
            budget=10000
        )

        category1 = Category.objects.create(
            project=project2,
            name='development'

        )

        Expense.objects.create(

            project=project2,
            title='expense 1',
            amount=5000,
            category=category1

        )

        Expense.objects.create(

            project=project2,
            title='expense 2',
            amount=2000,
            category=category1

        )
        self.assertEquals(project2.total_transactions,2)
