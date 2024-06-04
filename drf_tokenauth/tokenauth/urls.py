from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register( 'studentmodelsessionauth', views.StudentmodelViewsetSessionAuth, basename='studentmodelsessionauth')

urlpatterns = [
    path("", include(router.urls)),
    path ("auth/", include( 'rest_framework.urls', namespace='rest_framework')),
    path("gettoken/", views.CrateTokenView.as_view()),
    path("getjwttoken/", TokenObtainPairView.as_view()),
    path("refreshjwttoken/", TokenRefreshView.as_view()),
    path("verifyjwttoken/", TokenVerifyView.as_view()),
    
]
