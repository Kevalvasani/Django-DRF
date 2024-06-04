from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly



'''
    normal Viewset
'''
class StudentviewSet(viewsets.ViewSet):
    def list(self,request):
        print("===============list================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def retrieve(self,request,pk = None):
        print(pk)
        print("===============Retrieve================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        if id is not None:
            stu = Student.objects.filter(id=id)
            if stu.exists():
                serializer = StudentSerializer(stu, many = True)
                return Response(serializer.data)
            else:
                return Response("Student not found")
    
    def create(self,request):            
        print("===============Create================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)    
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk = None):
        print("===============Update================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk=None):
        print("===============Partial Update================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk):
        print("===============Distroy================")
        print("Basename : ",self.basename)
        print("Actions :",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted','status':status.HTTP_201_CREATED})
    
    
'''
    ModelViewsets
'''
class StudentmodelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
'''
    Readonly method 
'''
class StudentReadonlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

'''
    Authentication
'''
class StudentmodelViewsetAuth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]    # All Authenticated users can access this API
    # permission_classes = [IsAdminUser]        # Only Admin users can access this API
    permission_classes = [AllowAny]             # All Authenticated and non Authenticated user can also access this API

'''
    Session Authentication
'''
class StudentmodelViewsetSessionAuth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]   
    # permission_classes = [IsAdminUser]       
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]   # All user cane access this API but Those who are not login then they are not allow to post and delete and update
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]