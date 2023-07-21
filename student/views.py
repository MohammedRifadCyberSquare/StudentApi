from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def register_student(request):
    try:

        params = request.data # fetching post data
        serialized_data = StudentSerializer(data = params) # serializing post data

        if serialized_data.is_valid(): # checking if the serialized data is valid or not. It is mandatory
            serialized_data.save()

            return Response({'message': 'Student Registered Successfully','statusCode': 201})

        else:
            return Response({'message': 'Form Not Valid', 'statusCode': 403})

    except:
        return Response({'message': 'Something Went Wrong','statusCode': 500})





@api_view(['GET'])
def students_list(request):
    student_data = Student.objects.all() # fetching data model
      # serializing query set, many = true is passed when serializing multiple data
    serialized_data = StudentSerializer(student_data, many = True)
    return Response({'Students': serialized_data.data, 'statusCode': 201})


@api_view(['GET'])
def student_details(request, id):
    try:
        student_data = Student.objects.get(id = id) 
        
        serialized_data = StudentSerializer(student_data)

    except:
        return Response({'message': 'No Data Found', 'statusCode': 404})

    return Response({'Students': serialized_data.data, 'statusCode': 201})


@api_view(['PUT'])
def update_student(request, id):
    params = request.data
    student_data = Student.objects.get(id = id)
    serialized_data = StudentSerializer(student_data, data = params) # serializing corresponding data
    
    try:
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'message': 'Details Updated Succesfully', 'statusCode': 201})
        else:
            return Response({'message': 'Form Not Valid', 'statusCode' : 403})
    except:
        
        return Response({'message': 'Something Went Wrong', 'statusCode': 500})



@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_data = Student.objects.get(id = id)
        student_data.delete()

        return Response({'message': 'Succesfully Deleted', 'statusCode' :202})
    except:
        return Response({'message': 'No Data Found', 'statusCode': 404})