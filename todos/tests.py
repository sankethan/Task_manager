from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo=Todo.objects.create(
            title="test todo",
            body="to check weather its working or not",
        )
    def test_model_content(self):
        self.assertEqual(self.todo.title,"test todo")
        self.assertEqual(self.todo.body,"to check weather its working or not")
        self.assertEqual(str(self.todo),"test todo")
    def test_api_listview(self): # new
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    def test_api_detailview(self): # new
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first Todo")
