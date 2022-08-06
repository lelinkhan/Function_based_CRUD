from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def home(request):
    all_student = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()
    return render(request, 'home.html', {'all_student': all_student, 'form': form})


def edit_student(request, id):
    all_student = Student.objects.all()
    form = StudentForm()
    obj = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/', obj.id)
    else:
        form = StudentForm(instance=obj)
    return render(request, 'home.html', {'all_student': all_student, 'form': form})


def delete_student(request, id):
    if request.method == 'POST':
        dl = Student.objects.get(id=id)
        dl.delete()
        return HttpResponseRedirect('/')
