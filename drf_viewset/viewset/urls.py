from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register( 'student', views.StudentviewSet, basename='student')
router.register( 'studentmodel', views.StudentmodelViewset, basename='studentmodel')
router.register( 'studentmodelreadonly', views.StudentReadonlyModelViewSet, basename='studentmodelreadonly')
router.register( 'studentmodelauth', views.StudentmodelViewsetAuth, basename='studentmodelauth')
router.register( 'studentmodelsessionauth', views.StudentmodelViewsetSessionAuth, basename='studentmodelsessionauth')

urlpatterns = [
    path("", include(router.urls)),
    path ("auth/", include('rest_framework.urls', namespace='rest_framework')),
]
