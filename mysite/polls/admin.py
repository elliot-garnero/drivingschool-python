from django.contrib import admin

from .models import Student, Instructor, Meeting


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

class InstructorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['lastName']}),
        (None,               {'fields': ['firstName']}),
    ]
    # inlines = [ChoiceInline]
    search_fields = ['lastName']


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['instructor']}),
        (None,               {'fields': ['lastName']}),
        (None,               {'fields': ['firstName']}),
    ]
    search_fields = ['lastName']


class MeetingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['instructor']}),
        (None,               {'fields': ['student']}),
        ('Date rendez-vous', {'fields': ['date']}),
        (None,               {'fields': ['place']}),
    ]
    search_fields = ['instructor']


admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Meeting, MeetingAdmin)
