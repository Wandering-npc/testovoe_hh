from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Post
from .serializers import PostSerializer


@extend_schema(
    description="Список всех постов пользователя",
    methods=["GET", "POST"],
    tags=["Блог"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить список постов",
    ),
    post=extend_schema(
        summary="Создать пост",
    )
)
class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """
        Получить список всех постов пользователя.
        """
        posts = Post.objects.filter(user=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Создать новый пост.
        
        Параметры:
        - user: Идентификатор пользователя, создающего пост.
        - title: Заголовок поста.
        - text: Текст поста.
        - published: Опубликован ли пост (true/false).
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["Пост"],
    description="Получить, обновить или удалить конкретный пост",
    methods=["GET", "PUT", "DELETE"],
    
)
@extend_schema_view(
    get=extend_schema(
        summary="Детальная информация о посте",
    ),
    put=extend_schema(
        summary="Отредактировать пост",
    ),
    delete=extend_schema(
        summary="Удалить пост",
    ),
)
class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

    def get(self, request, pk):
        """
        Получить информацию о конкретном посте.

        Параметры:
        - pk: Идентификатор поста.
        """
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Обновить информацию о конкретном посте.

        Параметры:
        - pk: Идентификатор поста.
        - title: Новый заголовок поста.
        - text: Новый текст поста.
        - published: Обновленное состояние публикации поста (true/false).
        """
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Удалить конкретный пост.

        Параметры:
        - pk: Идентификатор поста.
        """
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

