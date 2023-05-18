from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *
from pyresparser import ResumeParser

import json
import en_core_web_sm
from test_code import test
import mimetypes

def resume_data(path):
    data = ResumeParser(path).get_extracted_data()
    name=data["name"]
    email=data["email"]
    mob=data["mobile_number"]
    skills=data["skills"]
    experience=data["experience"]
    designation=data["designation"]
    degree=data["degree"]
    total_exp=data["total_experience"]
    companies=data["company_names"]
    name="Not Avilable" if name is None else name
    email="Not Avilable" if email is None else email
    mob="Not Avilable" if mob is None else mob
    skills="Not Avilable" if skills is None else skills
    experience="Not Avilable" if experience is None else experience
    designation="Not Avilable" if designation is None else designation
    degree="Not Avilable" if degree is None else degree
    total_exp="Not Avilable" if total_exp is None else total_exp
    companies="Not Avilable" if companies is None else companies
    data_json=json.dumps(data)
    return name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
    
     
 
    
def regi(request):
    return render(request,'register.html')    
    
    
    
def addreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=reg(name=name,email=email,password=password)
        user.save()
    return render(request,'register.html')
 

def dash(request):
    return render(request,'admin/index.html')
    
     
def login(request):
    return render(request,'login.html')
    
     
def logint(request):
    email = request. POST.get('email')
    password = request.POST.get('password')
   # print(email)
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['logintdetail'] = email
        request.session['logint'] = 'admin'
        print ("ello")
        return render(request, 'admin/index.html')

    elif reg.objects.filter(email=email,password=password).exists():
        userdetails=reg.objects.get(email=email, password=password)
        request.session['uid'] = userdetails.id
        
        return render(request,'index.html')  


        
    else:
        return render(request, 'login.html', {'status': 'INVALID USERID OR PASSWORD'})           


  
         
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)  

def viewjobadmin(request):
    sel=posts.objects.all()
    return render(request,'admin/viewjob.html',{'res':sel})


def viewapplications(request,id):
    sel=upload.objects.filter(job_id=id,skill_sim__gte=30.0)
    return render(request,'admin/viewapplications.html',{'res':sel})

def viewapplicationss(request,id):
    sel=upload.objects.filter(job_id=id)
    return render(request,'admin/viewapplicationss.html',{'res':sel})

def deletejobpost(request,id):
    post=posts.objects.get(id=id)
    post.delete()
    return redirect(viewjobadmin)


def post(request):
    sel=jobpost.objects.all()
    return render(request,'admin/jobpool.html',{'res':sel})
    
def addpost(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        date=request.POST.get('date')
        user=posts(name=name,description=description,date=date)
        user.save()
    #return render(request,'admin/joobpool.html')
    return redirect(post)

def jobrole(request):
    return render(request,'admin/jobrole.html')

def addjobrole(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        skills=request.POST.get('skills')
        print("skills:",skills)
        #date=request.POST.get('date')
        user=jobpost(name=name,description=description,skills=skills)
        user.save()
    return render(request,'admin/jobrole.html')
       


def viewpost(request):
    sel=posts.objects.all()
    return render(request,'viewjob.html',{'res':sel})     
    
           
       

def apply(request,id):
    sel=posts.objects.get(id=id)
    request.session['job_apply_name']=sel.name
    return render(request,'applyjoob.html',{'res':sel})     
    
    
"""def jobposts(request):
    if request.method == 'POST':
        job_id=request.POST.get('job_id')
        
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
       
        emp=upload(userid=request.session['uid'],job_id=job_id,image=filename)    
        emp.save()
    return render(request,'applyjoob.html')
   """ 
    
def jobposts(request):
    if request.method == 'POST':
        job_id=request.POST.get('job_id')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        print("flg1")
        name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json=resume_data("media/{}".format(myfile.name))
        sel=jobpost.objects.get(name=request.session['job_apply_name'])
        job_skills=sel.skills
        job_skills=job_skills.split(',')
        skill_cnt=0
        total_job_skills=len(job_skills)
        job_skills=[i.lower() for i in job_skills]
        skills=[i.lower() for i in skills]
        print("job skills:",job_skills)
        print("resume skills:",skills)
        for i in job_skills:
            if i in skills:
                skill_cnt+=1
        skill_sim=(skill_cnt/total_job_skills)*100
        print("flg2")
        print("DataType:",type(experience))
        print("jobskills:",job_skills)
        print("skills:",skills)
        print("skill similarity:",skill_sim)
        personality=test.predict("media/{}".format(myfile.name))
        #print(name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json,personality)
        user=upload(userid=request.session['uid'],job_id=str(job_id),name=name,email=email,phone=mob,skill=skills,experience=str(experience),jsondata=data_json,image=filename,personality=personality,skill_sim=skill_sim)
        user.save()
        #return render(request,'admin/viewresume.html')
        sel=posts.objects.all()
        return render(request,'viewjob.html',{'res':sel,'status':'registered succesfully'})
    
    
    
def viewjobpost(request):
    #sel=upload.objects.filter(skill_sim__gte=10)
    sel=upload.objects.all()
    return render(request,'admin/viewresume.html',{'res':sel})

def download_resume(request,resume):
    path = open("media/"+resume, 'rb')
    mime_type, _ = mimetypes.guess_type("media/"+resume)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % resume
    return response