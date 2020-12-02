from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Post, Group
from ..forms import PostForm



class PostFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title="Тестовый текст",
            slug="test-slug",
            description="Тестовое описание"
        )
        cls.group = Group.objects.get(id=1)

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test-user")
        self.authenticated_user = Client()
        self.authenticated_user.force_login(self.user)

    def test_correct_user(self):

        from_data = {
            "group": self.group,
            "text": "Тестовый текст",
        }
        tasks_count = Post.objects.count()
        response = self.authenticated_user.post(
            reverse("new_post"),
            data=from_data,
            follow=True

        )
        self.assertEqual(Post.objects.count(), tasks_count + 1)
        print(tasks_count)
        print(Post.objects.count())



