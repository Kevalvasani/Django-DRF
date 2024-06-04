from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# @api_view(['GET'])
# def get_api(request):
#     return Response({'msg': 'Hello'})


# @api_view(['GET','POST'])
# def post_api(request):
#     if request.method == 'GET':
#         print(request.data)
#         return Response({'msg': 'Hello Get'})
    
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'Hello Post','data':request.data})
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        print(id)
        if id is not None:
            s = Student.objects.filter(id=id)
            if s.exists():
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            return Response({'msg':'Student not found.'})
        stu = Student.objects.all()
        serializer =  StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def student_apiview(request,pk=None):
    if request.method == 'GET':
        id = pk
        print(id)
        if id is not None:
            s = Student.objects.filter(id=id)
            if s.exists():
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            return Response({'msg':'Student not found.','status':status.HTTP_201_CREATED})
        stu = Student.objects.all()
        serializer =  StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted','status':status.HTTP_201_CREATED})
    
    
    
    
'''
    Class Based APIView 
'''

class StudentClassAPIview(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        print(id)
        if id is not None:
            s = Student.objects.filter(id=id)
            if s.exists():
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            return Response({'msg':'Student not found.','status':status.HTTP_400_BAD_REQUEST})
        stu = Student.objects.all()
        serializer =  StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated','status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted','status':status.HTTP_201_CREATED})
    


'''
    Generic API View and Mixins
'''

class Studentlist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Studentcreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class Studentretrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
class Studentupdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
class Studentdestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
'''
    List and create -> PK not required 
'''
class Student_l_c(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


# Retrive, Update and Destroy -> PK required
class Student_r_u_d(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
'''
    Concrete API for List and Create
'''  
class Student_c_l(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Student_c_c(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class Student_c_l_c(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
'''
    Concrete API for Retrieve and Update and Destroy
''' 
class Student_c_r(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Student_c_u(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class Student_c_d(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class Student_c_r_u_d(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer