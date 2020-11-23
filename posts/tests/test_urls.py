from django.test import TestCase, Client

class StaticURLTests(TestCase):

    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()


    def test_homepage(self):
        # Делаем запрос к главной странице и проверяем статус
        response = self.guest_client.get('/')
        # Утверждаем, что для прохождения теста код должен быть равен 200
        self.assertEqual(response.status_code, 200)

    def test_new_page(self):
        response = self.guest_client.get("/new/")
        self.assertEqual(response.status_code, 200)

    # def test_author_page(self):
    #     response = self.guest_client.get("/signup/")
    #     self.assertEqual(response.status_code, 200)