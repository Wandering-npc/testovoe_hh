from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

class TestsPostsAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_post(self):
        url = '/api/posts/'
        data = {
            'user': self.user.id,
            'title': 'Тестовый Заголовок',
            'text': 'Тестовый Текст',
            'published': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Тестовый Заголовок')

    def test_get_posts(self):
        url = '/api/posts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_post(self):
        post = Post.objects.create(user=self.user, title='Тестовый Заголовок', text='Тестовый Текст', published=True)
        url = f'/api/posts/{post.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Тестовый Заголовок')

    def test_update_post(self):
        post = Post.objects.create(user=self.user, title='Тестовый Заголовок', text='Тестовый Текст', published=True)
        url = f'/api/posts/{post.id}/'
        data = {'title': 'Обновленный Тестовый Заголовок', 'text': 'Обновленный Тестовый Текст', 'published': False}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=post.id).title, 'Обновленный Тестовый Заголовок')
    
    def test_delete_post(self):
        post = Post.objects.create(user=self.user, title='Test Title', text='Test Text', published=True)
        url = f'/api/posts/{post.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
