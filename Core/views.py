from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    student_list = Student.objects.all()
    return render(request, 'home.html', {"student_list": student_list})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        register_num = request.POST.get('register_num')

        if Student.objects.filter(register_num=register_num).exists():
            error_message = "A student with this register number already exists."
            return render(request, 'add_student.html', {"error_message": error_message})
        
        student = Student(name=name, branch=branch, register_num=register_num)
        student.save()
        return redirect("home")
    return render(request, "add_student.html")


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        register_num = request.POST.get('register_num')

        if Student.objects.filter(register_num=register_num).exclude(id=student_id).exists():
            error_message = "A student with this register number already exists."
            return render(request, 'update_student.html', {"student": student, "error_message": error_message})
        
        student.name = name
        student.branch = branch
        student.register_num = register_num
        student.save()
        return redirect("home")
    return render(request, 'update_student.html', {"student": student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("home")