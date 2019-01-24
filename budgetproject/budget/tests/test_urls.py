from django.test import SimpleTestCase
from django.urls import reverse,resolve

from budget.models import Project,Category,Expense
from budget.views import project_list,project_detail,ProjectCreateView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse("list")
        self.assertEquals(resolve(url).func,project_list)

    def test_project_create_url_is_resolved(self):
        url = reverse("add")
        self.assertEquals(resolve(url).func.view_class,ProjectCreateView)

    def test_project_detail_url_is_resolved(self):
        url = reverse("detail",args=["library-management"])
        self.assertEquals(resolve(url).func,project_detail)



