from django.urls import path, include
from rest_framework.routers import DefaultRouter

from challenge import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewset, basename='categories')
router.register(r'files', views.FileViewSet, basename='files')
router.register(r'', views.ChallengeViewset, basename='challenges')

urlpatterns = [
    path('submit_flag/', views.FlagSubmitView.as_view(), name='submit-flag'),
    path('', include(router.urls)),
]
