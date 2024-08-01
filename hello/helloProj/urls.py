"""
URL configuration for helloProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from helloApp import views
from helloApp.views import aheadcurdatetime, beforecurdatetime, curdatetime, dynabcdt, dynacdt, dynbcdt, fruit_student_list, generatetable, getstudentdata, home, aboutus, contactus, studentlist, courselist, register, enrolledlist, addproject, studentlistview, sayhello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',sayhello),
    path('cdt/',curdatetime),
    path('acdt/',aheadcurdatetime),
    path('bcdt/',beforecurdatetime),
    path('dynacdt/<int:t>/',dynacdt),
    path('dynbcdt/<int:t>/',dynbcdt),
    path('dynabcdt/<str:t>/',dynabcdt),
    path('tables/<int:num1>/<int:num2>/',generatetable),
    path('fslist/',fruit_student_list),
    path('getstudentdata/',getstudentdata),
    path('home/',home),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('studentlist/',studentlist),
    path('courselist/',courselist),
    path('register/',register),
    path('enrolledlist/',enrolledlist),
    path('addproject/',addproject),
    path('studentlistview/',studentlistview.as_view()),

]
