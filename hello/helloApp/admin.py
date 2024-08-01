from django.contrib import admin
from helloApp.models import student, course

# Register your models here.
#admin.site.register(student)
#admin.site.register(course)

admin.site.site_header="BTI Administration Portal"
admin.site.site_title="Admin Portal"
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'sem')
    ordering=('usn', 'name')
    search_fields=('usn',)
    
@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseTitle', 'courseCredits')
    ordering=('courseCode',)
    search_fields=('courseCode','courseTitle')
    

    
