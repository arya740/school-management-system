from django.contrib import admin
from .models import Branch, AcademicYear, SchoolClass, Subject, TeacherAssignment

admin.site.register(Branch)
admin.site.register(AcademicYear)
admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(TeacherAssignment)
