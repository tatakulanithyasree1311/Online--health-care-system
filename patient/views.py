from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Patient
from.models import Doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

def insertview(request):
    if request.method=='GET':
        return render(request,'patient/home.html')
    if request.method=='POST':
        pid=int(request.POST['pid'])
        pname=request.POST['pname']
        paddress=request.POST['paddress']
        pphone=int(request.POST['pphone'])
        pdisease=request.POST['pdisease']
        pemail=request.POST['pemail']
        doc_designation=request.POST['doc_designation']
        presult=request.POST['presult']
        pobj=Patient(pid=pid,pname=pname,paddress=paddress,pphone=pphone,pdisease=pdisease,pemail=pemail,doc_designation=doc_designation,presult=presult)
        pobj.save()
        return render(request,'patient/home.html',{'msg':'inserted sucessfully...' })
def selectview(request):
    if request.method=='GET':
        pati=Patient.objects.all()
        return render(request, 'patient/record.html', {'data': pati})
def updatepatient(request, pid):
    if request.method=='GET':
        pobje=Patient.objects.filter(pid=pid).first()
        return render(request,'patient/update.html',{'patient':pobje})
    if request.method=='POST':
        pid=int(request.POST['pid'])
        pname=request.POST['pname']
        paddress=request.POST['paddress']
        pphone=int(request.POST['pphone'])
        pdisease=request.POST['pdisease']
        pemail=request.POST['pemail']
        doc_designation=request.POST['doc_designation']
        presult=request.POST['presult']
        Patient.objects.filter(pid=pid).update(pid=pid,pname=pname,paddress=paddress,pphone=pphone,pdisease=pdisease,pemail=pemail,doc_designation=doc_designation,presult=presult)        
        return redirect('/page3/record/')
def deletepatient(request,pid):
    if request.method=='GET':
        pat=Patient.objects.get(pid=pid)
        return render(request,'patient/delete.html',{'patient':pat})
    if request.method=='POST':
        pat=Patient.objects.get(pid=pid).delete()
        return redirect('/page3/record/')
def signupview(request):
     if request.method=='GET':
         emptyform=UserCreationForm()
         return render(request,'patient/signup.html',{'&form':emptyform})
     if request.method=='POST':
         dataform=UserCreationForm(request.POST)
         if dataform.is_valid()==True:
             dataform.save()
             return redirect('loginurl')
         else:
             return render(request,'patient/signup.html',{'form':dataform})
def loginview(request):
    if request.method=='GET':
        return render(request,'patient/login.html')
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        valid_user=authenticate(request,username=uname,password=pwd)
        if valid_user==None:
            return redirect('loginurl')
        else:
            return redirect('optionurl')
def mainview(request):
    if request.method=='GET':
        return render(request,'patient/main.html')
def optionview(request):
    if request.method=='GET':
        return render(request,'patient/option.html')
def insert1(request):
    if request.method=='GET':
        return render(request,'patient/doc_insert.html')
    if request.method=='POST':
        did=int(request.POST['did'])
        dname=request.POST['dname']
        dqualification=request.POST['dqualification']
        dspecilization=request.POST['dspecilization']
        ddesignation = request.POST['ddesignation']
        dexperience=request.POST['dexperience']
        sal=int(request.POST['sal'])
        dobj=Doctor(did=did,dname=dname,dqualification=dqualification,dspecilization=dspecilization,ddesignation=ddesignation,dexperience=dexperience,sal=sal)
        dobj.save()
        return render(request,'patient/doc_insert.html',{'msg':'inserted sucessfully...' })
def selectview1(request):
    if request.method=='GET':
        doc=Doctor.objects.all()
        return render(request, 'patient/doc_record.html', {'doctor': doc}) 
         