from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from console_geeks_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        favourites_count=Count('favourites', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    filterset_fields = [
        'category',
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'favourites__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'favourites_count',
        'likes_count',
        'comments_count',
        'favourites__created_at'
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        favourites_count=Count('favourites', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')