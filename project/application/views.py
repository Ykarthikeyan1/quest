from django.shortcuts import render,redirect,HttpResponse
from .models import register,Project,Task,Ticket

from django.db import connection



def projectstatus(request):
    cursor=connection.cursor()
    cursor.execute("select Project_Id ,Project_Name ,Description ,application_ticket.Task_Id ,Tasks_Name,Ticket_Id ,Ticket_Name,Assigned_Date ,Deadline_Date ,Developer_Name , Dev_des ,Status from application_project join application_task on application_task.Project_Id =application_project.id join application_ticket on application_ticket.Task_Id=application_task.Task_Id;")
    result=cursor.fetchall()

    return render(request, 'projectstatus.html', {'a': result})

def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = register()
        users.Name = name
        users.Address = address
        users.Username = username
        users.Password = password
        users.save()

    return render(request,'registerpage.html')
def devlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            register.objects.get(Username=username,Password=password)
            return redirect('/devpending/'+username)
        except:
            return HttpResponse('invalids user')

    return render(request,'devlogin.html')

def tllogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'tl' and password == '1':
            return redirect('/tlpending/')
        else:
            return HttpResponse('invalid ')

    return render(request,'tllogin.html')
def managerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'manager' and password == '1':
            return redirect('/projectregister/')
        else:
            return HttpResponse('invalid ')

    return render(request,'managerlogin.html')
def projectregister(request):
    if request.method == 'POST':
        project_name = request.POST.get('name')
        description = request.POST.get('description')
        Assigned_Date = request.POST.get('adate')
        Deadline_Date = request.POST.get('ddate')
        users = Project()
        users.Project_Name = project_name
        users.Description = description
        users.Assigned_Date = Assigned_Date
        users.Deadline_Date = Deadline_Date
        users.Status = "pending"
        users.save()
    return render(request,'projectregister.html')
def projectassin(request):
    datas=Project.objects.filter(State=0)
    return render(request,'projectassin.html',{'value':datas})
def projecttlassin(request,id):
    user = Project.objects.get(id=id)
    user.State = 1
    user.save()
    return redirect('/projectassin')
def projectedit(request,id):
    details = Project.objects.filter(id=id)
    data = Project.objects.get(id=id)
    if request.method =='POST':
        project_name = request.POST.get('name')
        description = request.POST.get('description')
        Assigned_Date = request.POST.get('adate')
        Deadline_Date = request.POST.get('ddate')
        data.Project_Name = project_name
        data.Description = description
        data.Assigned_Date = Assigned_Date
        data.Deadline_Date = Deadline_Date
        data.Status = "pending"
        data.save()
        return redirect('/projectassin')
    return render(request,'projectassin.html',{'value':details,'a':data})
def projectdelete(request,id):
    Project.objects.get(id=id).delete()
    return redirect('/projectassin')

def tlpending(request):
    datas=Project.objects.filter(State=1)
    return render(request,'tlpending.html',{'value':datas})
def projectcompleted(request,id):
    user = Project.objects.get(id=id)
    user.State = 2
    user.Status="Completed"
    user.save()
    return redirect('/tlpending')
def taskregister(request,id):
    details=Project.objects.filter(id=id)
    if request.method =='POST':
        task = request.POST.get('task')
        datas = Task()
        datas.Project_Id=id
        datas.Tasks_Name=task
        datas.State=0
        datas.save()
        last_rowd = Task.objects.last()
        tid = last_rowd.id
        pid=last_rowd.Project_Id
        last_rowd.Task_Id=str(pid)+(',')+str(tid)
        last_rowd.save()
        return redirect('/tlpending')
    return render(request,'tlpending.html',{'value':details,'a':'a'})
def ticketpending(request):
    datas=Task.objects.filter(State=0)
    return render(request,'ticketpending.html',{'value':datas})
def ticketregister(request,Task_Id):
    datas=Task.objects.filter(Task_Id=Task_Id)
    data=register.objects.all()
    if request.method =='POST':
        ticket = request.POST.get('ticket')
        name = request.POST.get('developer')
        datars = Ticket()
        datars.Task_Id=Task_Id
        datars.Developer_Name=name
        datars.Ticket_Name = ticket
        datars.State=0
        datars.save()
        last_rowd = Ticket.objects.last()
        tid = last_rowd.id
        pid=last_rowd.Task_Id
        last_rowd.Ticket_Id=str(pid)+(',')+str(tid)
        last_rowd.save()
        return redirect('/ticketpending')

    return render(request,'ticketpending.html',{'value':datas,'a':data})
def devpending(request,username):
    datas = Ticket.objects.filter(State=0,Developer_Name=username)
    return render(request, 'devpending.html', {'value': datas})
def devcom(request,id,username):
    details = Ticket.objects.filter(id=id)
    data = Ticket.objects.get(id=id)
    if request.method =='POST':
        devsigns = request.POST.get('sign')
        data.Dev_des = devsigns
        data.State = 1
        data.save()
        return redirect('/devpending/'+username)
    return render(request,'devpending.html',{'value':details,'a':data})
def tlchecking(request):
    datas = Ticket.objects.filter(State=1)
    return render(request, 'tlchecking.html', {'value': datas})
def tlapprove(request,id):
    user = Ticket.objects.get(id=id)
    user.State = 2
    user.Status="completed"
    user.save()
    return redirect('/tlcheking')
def tldenied(request,id):
    user = Ticket.objects.get(id=id)
    user.State = 0
    user.Status="completed"
    user.save()
    return redirect('/tlcheking')
def ticketcomleted(request,id):
    user = Task.objects.get(id=id)
    user.State = 2
    user.Status="completed"
    user.save()
    return redirect('/ticketpending')

def view(request,id,id1,id2,id3):
    details=Project.objects.filter(id=id)
    data=Task.objects.filter(Task_Id=id1)
    datab=Ticket.objects.filter(Ticket_Id=id2)
    datac=register.objects.filter(Username=id3)
    return render(request,'view.html',{'value':details,'a':data,'b':datab,'c':datac})

