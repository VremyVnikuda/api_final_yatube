from django.urls import path, include
from rest_framework import routers

import api.views as vs

router_v1 = routers.DefaultRouter()
router_v1.register(
    'groups',
    vs.GroupViewSet,
    basename='groups',
)
router_v1.register(
    'posts',
    vs.PostViewSet,
    basename='posts',
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    vs.CommentViewSet,
    basename='comments',
)
router_v1.register(
    'follow',
    vs.FollowViewSet,
    basename='follow',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
