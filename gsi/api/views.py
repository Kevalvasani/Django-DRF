from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer,Studentmodelserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu=Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

'''
    Function based API's For student
'''
@csrf_exempt
def student_fun_api(request):
    '''
        Data GET request
    '''
    '''       
        Data PUT(Update) request
    '''
    '''       
        Data GET request
    '''
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)    
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    # if request.method == "GET":
    #     id = request.GET.get('id',None)
    #     if id is not None:
    #         try:
    #             stu = Student.objects.get(id=id)
    #             serializer = StudentSerializer(stu)
    #             json_data = JSONRenderer().render(serializer.data)
    #             return HttpResponse(json_data, content_type='application/json')
    #         except:
    #             res = {'msg':'Student Not Found'}
    #             return JsonResponse(res,status=404)
    #     else:
    #         stu = Student.objects.all()
    #         serializer = StudentSerializer(stu, many=True)
    #         json_data = JSONRenderer().render(serializer.data)
    #         return HttpResponse(json_data, content_type='application/json')
   
    '''       
        Data POST request
    '''
    if request.method == "POST":
        json_data = request.body
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    '''       
        Data PUT(Update) request
    '''
    if request.method=="PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    '''       
        Data DELETE request
    '''
    if request.method == "DELETE":
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted!'}
        # json_data = JSONRenderer().render(res)
        # print(json_data)
        # return HttpResponse(json_data,content_type='application/data')
        return JsonResponse(res,safe=False)
    


'''
    Class based API's For student
'''
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    
    '''       
        Data GET request
    '''
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)    
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    '''
        Data POST request
    '''
    def post(self,  request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    '''       
        Data PUT(Update) request
    '''
    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    '''      
       Data DELETE request
    '''
    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

'''
    Modelserializer is used in class
'''
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIModel(View):
    
    '''       
        Data GET request
    '''
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)    
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentmodelserializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = Studentmodelserializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    '''
        Data POST request
    '''
    def post(self,  request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Studentmodelserializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    '''       
        Data PUT(Update) request
    '''
    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = Studentmodelserializers(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    '''      
       Data DELETE request
    '''
    
    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = Studentmodelserializers(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


    
    
    
    
    
    


