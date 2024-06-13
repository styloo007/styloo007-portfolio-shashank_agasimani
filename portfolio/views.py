from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience, Education, Certification, Publication, Skill
import smtplib 
import random
import time
import string


def index(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    publications = Publication.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio/index.html', {
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
        'publications': publications,
        'skills': skills,
    })



def contactme(request):
    if request.method=='POST':
        name=request.POST.get('name')
        emaill=request.POST.get('email')
        sub=request.POST.get('subject')
        message=request.POST.get('message')
        
        

        print(name)
        print(emaill)
        print(sub)
        print(message)
        
        
        email="cloudverse.easystudent@gmail.com"
        rec_email='shashankagasimani2@gmail.com'

        subject= sub
        
        server=smtplib.SMTP("smtp.gmail.com",587)
        
        
        text=f"Portfolio Contact: {name}\n\n{emaill}\n\n{subject}\n\n{message}"

        server.starttls()

        server.login(email, "omxw siwn buax zeoh")

        server.sendmail(email, rec_email, text)

        print("Email sent to "+rec_email)
        
        
        
        
        
        
        
    return render(request, 'portfolio/index.html')


def project1(request):
    
    return render(request, 'project1.html')
def project4(request):
    
    return render(request, 'project2.html')
def project4(request):
    return render(request, 'project3.html')


def project4(request):
    return render(request, 'project4.html')
        