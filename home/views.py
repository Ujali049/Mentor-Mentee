from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def mentor_reg(request):  # for mentor registration
    return render(request,"AsMentor.html")

def mentee_reg(request):   # for mentee registration
    return render(request,"AsMentee.html")

def about(request):
    return render(request,"about.html")
def projects(request):
    return render(request,"projects.html")
def projects_details(request):
    return render(request,"projects_details.html")
def services(request):
    return render(request,"services.html")
def blog(request):
    return render(request,"blog.html")
def blog_details(request):
    return render(request,"blog-details.html")
def contact(request):
    return render(request,"contact.html")
