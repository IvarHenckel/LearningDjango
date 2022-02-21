from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course
from .forms import CourseModelForm

# Mixins aloows us to extend class based views with new code

class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

# Note that there is quite a lot of code duplication in this file
# This is beuase this is an example of raw class based views. In the blog app we use built in CreateView/UpdateView etc and get rid of a lot of code.
class CourseDeleteView(CourseObjectMixin, View): # The order matters
    template_name = 'courses/course_delete.html'
    # def get_object(self): by including the Mixin we no can move out code
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'
    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseModelForm()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {
            "form":form,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm() # reinitialize the form to open up a new empty create page
        context = {
            "form":form,
        }
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset()
        }
        return render(request, self.template_name, context)

class MyListView(CourseListView): # This way we can inherit  and built new features on top, other filtering in this case
    queryset = Course.objects.filter(id=1)

class CourseView(CourseObjectMixin, View): # Two ways of doing the same thing but with Class Based view vs Function based view. 
    # def get(self, request, *args, **kwargs): # Note that with a class based view the names actually matters
    #     return render(request, 'about.html', {})
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs): # Note that with a class based view the names actually matters
        context = {}
        if id is not None:
            obj = self.get_object() #get_object_or_404(Course, id=id) now handled by the mixin
            context['object'] = obj
        return render(request, self.template_name, context) # One advantage with using class based views is that by inheriting from other classes we can use a lot of built in mechanics. In this example we can specify in view.py wheter we want another template name for example.
    
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})