from django.shortcuts import render, redirect

from employee.forms import EmployeeForm

from employee.models import Employee

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm()  # Initialize form for GET request
    
    # Return the form for both GET and POST requests
    return render(request, 'index.html', {'form': form})

def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html',{'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'employee':employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
    


# Create your views here.
