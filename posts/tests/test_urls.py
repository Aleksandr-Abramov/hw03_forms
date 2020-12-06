from django.test import TestCase, Client
from ..models import Group, Post, User
from django.contrib.auth import get_user_model


class StaticURLTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title="Название группы",
            slug="test-slug",
            description="тестовый текст"
        )

        cls.group = Group.objects.get(id=1)

        cls.page_urls = {
            "/": "index.html",
            "/new/": "new.html",
            "/group/{}/".format(StaticURLTests.group.slug): "group.html"
        }

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="Alex")
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_available_pages(self):

        for page, template in StaticURLTests.page_urls.items():
            response = self.authorized_client.get(page)
            self.assertEqual(response.status_code, 200,
                             "Зарегистрированный пользователь, не смог войти.")

        for page, template in StaticURLTests.page_urls.items():
            response = self.guest_client.get(page)
            self.assertEqual(response.status_code, 200,
                             "Незарегистрированный пользователь, не смог войти.")

    def test_page_templates(self):
        for page, template in StaticURLTests.page_urls.items():
            with self.subTest():
                response = self.authorized_client.get(page)
                self.assertTemplateUsed(response, template,
                                        "{} данный шаблон не работает".format(template))
#
#     # Редирект
#     # def test_static_new_page_redirect(self):
#     #     response = self.guest_client.get('/new/', follow=True)
#     #     self.assertRedirects(response, '/new/?next=/index/')
