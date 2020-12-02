from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..forms import PostForm

from ..models import Post, Group


class ViewsTemplatesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title="Лев Толстой",
            slug="leo",
            description="текст"
        )

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='StasBasov')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_index_page_correct_template(self):
        response = self.authorized_client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_new_page_correct_template(self):
        response = self.authorized_client.get(reverse("new_post"))
        self.assertTemplateUsed(response, "new.html")

    def test_group_page_correct_template(self):
        response = self.authorized_client.get(reverse("group_posts", kwargs={"slug": "leo"}))
        self.assertTemplateUsed(response, "group.html")


class ViewPageContextTest(TestCase):



    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='Stas')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.group = Group.objects.create(
            title="Тестовые данные"
        )
        self.post = Post.objects.create(
            text="Тестовый текст!",
            author=self.user,
            group=self.group
        )

    def test_index_page_correct_context(self):
        response = self.authorized_client.get(reverse("index"))
        test_text = response.context.get("posts")[0].text
        test_author = response.context.get("posts")[0].author.username
        test_group = response.context.get("posts")[0].group.title
        self.assertEqual(test_text, "Тестовый текст!")
        self.assertEqual(test_author, "Stas")
        self.assertEqual(test_group, "Тестовые данные")
