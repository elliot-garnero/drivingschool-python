from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Instructor, Student, Secretary, Meeting


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['instructor_list'] = Instructor.objects.all()
        return context


class DetailViewStudent(generic.DetailView):
    model = Student
    template_name = 'polls/detailStudent.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailViewStudent,
                        self).get_context_data(*args, **kwargs)
        context['meeting_list'] = Meeting.objects.filter(
            student=self.kwargs['pk'])
        return context


class DetailViewInstructor(generic.DetailView):
    model = Instructor
    template_name = 'polls/detailInstructor.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailViewInstructor,
                        self).get_context_data(*args, **kwargs)
        context['student_list'] = Student.objects.filter(
            instructor=self.kwargs['pk'])
        context['meeting_list'] = Meeting.objects.filter(
            instructor=self.kwargs['pk'])
        return context


class MeetingView(generic.DetailView):
    model = Meeting
    template_name = 'polls/meeting.html'


class MeetingListView(generic.ListView):
    template_name = 'polls/meeting-list.html'
    context_object_name = 'meeting_list'

    def get_queryset(self):
        return Meeting.objects.all()
