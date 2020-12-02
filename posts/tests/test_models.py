from django.test import TestCase
from ..models import Post, Group
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModelGroup(TestCase):

    def setUp(self):
        Group.objects.create(
            title="Заголовок тестовой задачи",
        )

        self.db_data = Group.objects.get(pk=1)

    def test_title_label(self):
        test_data = self.db_data.__str__()
        expect_data = self.db_data.title
        self.assertEqual(expect_data, test_data)


class TestModelPost(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='IvanIvanov'
        )
        self.group = Group.objects.create(
            title="Тестовые данные"
        )
        self.post = Post.objects.create(
            text="Тестовый текст!",
            author=self.user,
            group=self.group
        )

    def test_title_label_post(self):
        test_data = self.post.__str__()
        expect_data = self.post.text
        self.assertEqual(expect_data, test_data)
