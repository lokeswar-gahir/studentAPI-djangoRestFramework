from rest_framework import serializers
from .models import *


def contains_digits_or_special_character(string):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    digits = "0123456789"
    for c in special_characters+digits:
        if c in string:
            return True
    return False


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name', 'age']
        # exclude = ['id', 'image']

    def validate(self, data):
        name = data.get('name')#.strip()
        if name:
            if contains_digits_or_special_character(data['name']):
                raise serializers.ValidationError(
                    {"name": "name should only contain alphabetic charachers !!!"})

        age = data.get('age')
        if age or age==0:
            if age > 110 or age < 0:
                raise serializers.ValidationError({"age": "Invalid age !!!"})
            elif age < 18:
                raise serializers.ValidationError(
                    {"age": "age less than 18 is not allowd !!!"})

        # phone_no = str(data.get('phone_no'))
        phone_no = data.get('phone_no')
        if phone_no:
            phone_no = str(phone_no)
            if not phone_no.isdigit() or len(phone_no) != 10:
                raise serializers.ValidationError(
                    {"phone_no": "phone numbers with only 10-digits(XXXXXXXXXX) are allowed !!!"})
            data['phone_no']="+91-"+phone_no
        
        return data
