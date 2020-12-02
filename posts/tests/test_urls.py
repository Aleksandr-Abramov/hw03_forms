from django.test import TestCase, Client
from ..models import Group, Post, User
from django.contrib.auth import get_user_model


class StaticURLTests(TestCase):
    # Тестовые данные
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title="Тестовый текст",
            slug="test-slug",
            description="Тестовое описание"
        )

    # Регистрация пользователя Alex и анонима
    def setUp(self):
        self.guest_client = Client()
        self.user = get_user_model().objects.create_user(username="Alex")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # Статические страницы
    def test_static_homepage_(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_static_new_page(self):
        response = self.guest_client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_static_group_page(self):
        response = self.guest_client.get("/group/test-slug/")
        self.assertEqual(response.status_code, 200)

    # шаблоны страниц
    def test_static_homepage_template(self):
        response = self.guest_client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_static_new_page_template(self):
        response = self.guest_client.get("/new/")
        self.assertTemplateUsed(response, 'new.html')

    def test_static_group_page_template(self):
        response = self.guest_client.get("/group/test-slug/")
        self.assertTemplateUsed(response, "group.html")

    # Редирект
    # def test_static_new_page_redirect(self):
    #     response = self.guest_client.get('/new/', follow=True)
    #     self.assertRedirects(response, '/new/?next=/index/')
