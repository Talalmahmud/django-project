from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def add(request):
    return render(request, 'add.html')

def addrecord(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    department = request.POST['department']

    students = Student(first_name= first_name, last_name= last_name, email= email, phone_number= phone_number, department= department)
    students.save()
    return HttpResponseRedirect(reverse('home'))

def show(request):
    students = Student.objects.all()
    context = {
        'students' : students,
    }

    return render(request, 'show.html', context)

def delete(request, id):
    student = Student.objects.get(id = id)
    student.delete()
    return HttpResponseRedirect(reverse('show'))

def update(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student' : student
    }
    return render(request, 'update.html', context)

def updaterecord(request, id):
    student = Student.objects.get(id = id)
    student.first_name = request.POST['first_name']
    student.last_name = request.POST['last_name']
    student.email = request.POST['email']
    student.phone_number = request.POST['phone_number']
    student.department = request.POST['department']
    student.save()
    return HttpResponseRedirect(reverse('show'))
