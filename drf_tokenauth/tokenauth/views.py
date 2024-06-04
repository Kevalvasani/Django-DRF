from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication


class CrateTokenView(ObtainAuthToken):
    """
    Create a new auth token for user.
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    
class StudentmodelViewsetSessionAuth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]   
    # permission_classes = [IsAuthenticatedOrReadOnly]

