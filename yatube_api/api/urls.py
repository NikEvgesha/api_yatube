from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')

comment_router_v1 = routers.NestedDefaultRouter(
    router_v1,
    'posts',
    lookup='post'
)
comment_router_v1.register(
    'comments',
    CommentViewSet,
    basename='post-comments'
)


urlpatterns_v1 = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
    path('', include(comment_router_v1.urls))
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1))
]
