from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Student
# Create your views here.

from .serializears import StudentSerializer

@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    serialstudents = StudentSerializer(students, many=True)
    return Response({
        'status':200,
        'students':serialstudents.data
    })

@api_view(['GET'])
def studentView(request, pk):
    try :
        student = Student.objects.get(id=pk)
        serialstudent = StudentSerializer(student, many=False)
        return Response({
            'status':200,
            'students':serialstudent.data,
        })
    except :
        return Response({'status':400})


@api_view(['POST'])
def studentAdd(request):
    try:
            
        serialdata = StudentSerializer(data=request.data)
        if serialdata.is_valid():
            serialdata.save()
        
        return Response({
            'status':200,
            'student':serialdata.data,
            'message':'Student added successfully'
        })

    except:
        return Response({'status':400})

@api_view(['POST'])
def studentUpdate(request, pk):
    try :
        student = Student.objects.get(id=pk)
        serialstudent = StudentSerializer(instance=student, data=request.data)

        if serialstudent.is_valid():
            serialstudent.save()
            
        return Response({
            'status':200,
            'student':serialstudent.data,
            'message':'Updated successfully'
        })

    except :
        return Response({'status':400})


@api_view(['DELETE'])
def studentdelete(request, pk):
    try:

        student = Student.objects.get(id=pk)
        student.delete()
        
        students = Student.objects.all()
        serialstudents = StudentSerializer(students, many=True)
        
        return Response({
            'status':200,
            'student':serialstudents.data,
            'message':'Student Deleted successfully'
        })

    except:
        return Response({'status':400})