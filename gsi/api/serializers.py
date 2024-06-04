from rest_framework import serializers
from .models import Student

"""
    Mostly used modelserializer
"""
class Studentmodelserializers(serializers.ModelSerializer):
    #validations 
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll']
        extra_kwargs = {'name': {'read_only': True}}


"""
    Mostly used modelserializer with another validiation
"""

# class Studentmodelserializers(serializers.ModelSerializer):
    
#     # validation for name with Staring alphabate R
#     def start_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError('Name should be start with R.')
    
#     name=serializers.CharField(max_length=100, validators=[start_with_r])
#     class Meta:
#         model = Student
#         fields = ['name','roll','city']
    
    # '''
    #     field level validation
    # '''
    # def validate_roll(self,value):
    #     print(value)
    #     if value > 20:
    #         raise serializers.ValidationError('Seal Full')
    #     return value
    
    # '''
    #     object level validation
    # '''
    # def validate(self,data):
    #     ct = data.get('city')
    #     if ct.lower()!='pune':
    #         raise serializers.ValidationError('City must be pune')
    #     return data
    
   

# Normal serializers    
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with R.')

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    '''
        Create student serializer
    '''
    def create(self,validate_data):
        
        return Student.objects.create(**validate_data)
    
    '''
        Update student serializer
    '''
    def update(self,instance,validate_data):
        print(instance.name)
        instance.name= validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll= validate_data.get('roll',instance.roll)
        instance.city= validate_data.get('city',instance.city)
        instance.save()
        return instance
    
    '''
        field level validation
    '''
    def validate_roll(self,value):
        print(value)
        if value > 20:
            raise serializers.ValidationError('Seal Full')
        return value
    
    '''
        object level validation
    '''
    def validate(self,data):
        ct = data.get('city')
        if ct.lower()!='pune':
            raise serializers.ValidationError('City must be pune')
        return data