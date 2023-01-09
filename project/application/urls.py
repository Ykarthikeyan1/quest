from django.urls import path
from . import views

urlpatterns=[
    path('',views.registerpage),
    path('devlog/', views.devlogin),
    path('managerlog/', views.managerlogin),
    path('tllog/', views.tllogin),
    path('projectregister/', views.projectregister),
    path('projectassin/', views.projectassin),
    path('projecttlassin/<int:id>', views.projecttlassin),
    path('projectedit/<int:id>', views.projectedit),
    path('projectdelete/<int:id>', views.projectdelete),
    path('projectstatus/', views.projectstatus),
    path('tlpending/', views.tlpending),
    path('projectcompleted/<int:id>', views.projectcompleted),
    path('taskregister/<int:id>', views.taskregister),
    path('ticketpending/', views.ticketpending),
    path('ticketregister/<str:Task_Id>', views.ticketregister),
    path('devpending/<str:username>', views.devpending),
    path('devcom/<int:id>/<str:username>', views.devcom),
    path('tlcheking/', views.tlchecking),
    path('tlapprove/<int:id>', views.tlapprove),
    path('tldenied/<int:id>', views.tldenied),
    path('ticketcomleted/<int:id>', views.ticketcomleted),
    path('view/<int:id>/<str:id1>/<str:id2>/<str:id3>/', views.view),


]
