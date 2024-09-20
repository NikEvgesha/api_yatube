from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

comment_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
comment_router.register('comments', CommentViewSet, basename='post-comments')


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('', include(comment_router.urls))
]
