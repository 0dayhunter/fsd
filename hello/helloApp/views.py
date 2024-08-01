import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#hello program
def sayhello(request):
    return HttpResponse("<h1>Hello Mam</h1>")

#current date and time
def curdatetime(request):
    dt=datetime.datetime.now()
    resp="<h1>Current Date and Time is %s</h1>"%(dt)
    return HttpResponse(resp)


#time ahead by 4 hours
def aheadcurdatetime(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=4)
    resp="<h1>Current Date and Time ahead by 4 hours is %s</h1>"%(dt)
    return HttpResponse(resp)

#before current date time
def beforecurdatetime(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=-4)
    resp="<h1>Current Date and Time before by 4 hours is %s</h1>"%(dt)
    return HttpResponse(resp)

#dynamic url
#ahead for n
def dynacdt(request,t):
    dt=datetime.datetime.now()+datetime.timedelta(hours=t)
    resp="<h1>Current Date and Time ahead by %d hours is %s</h1>"%(t,dt)
    return HttpResponse(resp)

#before n
def dynbcdt(request,t):
    dt=datetime.datetime.now()+datetime.timedelta(hours=-t)
    resp="<h1>Current Date and Time before by %d hours is %s</h1>"%(t,dt)
    return HttpResponse(resp)

#for both
def dynabcdt(request, t):
    t1 = int(t)
    dt = datetime.datetime.now() + datetime.timedelta(hours=t1)
    if t1 > 0:
        resp = "<h1>Current Date and Time Ahead by %d hours is %s</h1>"%(t1, dt)
    elif t1 < 0:
        resp = "<h1>Current Date and Time Before by %d hours is %s</h1>"%(t1, dt)
    else:
        resp = "<h1>No change detected</h1>"
    return HttpResponse(resp)

#table
def generatetable(request, num1,num2):
    resp=""
    for i in range(1,num2+1):
        resp+="<h3>%d X %d = %d</h3>"%(num1,i,num1*i)
    return HttpResponse(resp)
    

#list
def fruit_student_list(request):
    fl=['Mango','Apple','peas','orange']
    sl=['bhawesh','Adarsh','yuvraj','amod']
    return render(request,'fslist.html',{'Fruit_list':sorted(fl,key=len),'Student_list':sorted(sl)})

#student data
def getstudentdata(request):
    s1={'USN':'1BH21CS088','NAME':'SAHIL IQUBAL','SEM':6,'SEC':'B'}
    s2={'USN':'1BH21CS098','NAME':'SUBASH CHAUDHARY','SEM':6,'SEC':'B'}
    s3={'USN':'1BH21CS005','NAME':'ADRIEL ANTONY','SEM':6,'SEC':'A'}
    s4={'USN':'1BH21CS010','NAME':'AMOD YADAV','SEM':6,'SEC':'A'}
    s5={'USN':'1BH21CS004','NAME':'ADARSH ROY','SEM':6,'SEC':'A'}
    sl=[s1,s2,s3,s4,s5]
    return render(request,'studentlist.html',{'Student_List':sl})

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')


from helloApp.models import student,course
def studentlist(request):
    studentobjs=student.objects.all()
    return render(request,'studentlistfromdb.html',{'Student_List':studentobjs})

def courselist(request):
    courseobjs=course.objects.all()
    return render(request,'courselist.html',{'Course_List':courseobjs})

def register(request):
    if request.method=="POST":
        sid=request.POST.get('student')
        cid=request.POST.get('course')
        studentobj=student.objects.get(id=sid)
        courseobj=course.objects.get(id=cid)
        res=studentobj.courses.filter(id=cid)
        if res:
            resp="<h1>Student has already registered for this course</h1>"
            return HttpResponse(resp)
        else:
            studentobj.courses.add(courseobj)
            resp="<h1>Registration Successfull</h1>"
            return HttpResponse(resp)        
    else:    
        studentobjs=student.objects.all()
        courseobjs=course.objects.all()
        return render(request,'register.html',{'Student_List':studentobjs,'Course_List':courseobjs})
    
def enrolledlist(request):
    if request.method=="POST":
        cid=request.POST.get('course')
        courseobj=course.objects.get(id=cid)
        studentobjs=courseobj.student_set.all()
        completeCourseListobj=course.objects.all()
        return render(request,'enrolledlist.html',{'Enrolled_List':studentobjs,'Course_List':completeCourseListobj})       
    else:    
        courseobjs=course.objects.all()
        return render(request,'enrolledlist.html',{'Course_List':courseobjs})
    
from helloApp.forms import projectForm
def addproject(request):
    if request.method=="POST":
        frm=projectForm(request.POST)
        if frm.is_valid:
            frm.save()
            return HttpResponse("<h1>Project Added Successfully.</h1>")
        else:
            return HttpResponse("<h1>Please enter all the details.</h1>")
    else:
        frm=projectForm()
        return render(request,'addproject.html',{'form':frm})

from django.views import generic   
class studentlistview(generic.ListView):
    model=student
    template_name="studentlistview.html"
       