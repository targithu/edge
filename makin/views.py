from re import search
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin #when this is added in the leftcorner of inheritance list it would prevent access to the page unless and until you login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .forms import FeedbackForm
#username:thisit
#password:urpasswor

# Create your views here.
class CustomLoginView(LoginView):
   template_name='makin/login.html'#have to write app/templatename
   field='__all__'
   redirect_authenticated_user=True
   def get_success_url(self):
      return  reverse_lazy('first')
class RegisterPage(FormView):
   template_name='makin/register.html'
   form_class=UserCreationForm
   redirect_authenticated_user=True
   success_url=reverse_lazy('tasks') 
   #didn't understand below
   def form_valid(self,form):
      user=form.save()
      if user is not None:
         login(self.request,user)
         return super(RegisterPage,self).form_valid(form)
   def get(self,*args,**kwargs):
      if self.request.user.is_authenticated:
         return redirect('tasks')
      return super(RegisterPage,self).get(*args,**kwargs)
      #
class TaskList(LoginRequiredMixin,ListView):
   model = Task
   context_object_name="tasks"
   #didn't understand below
   def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      context['tasks']=context['tasks'].filter(name=self.request.user)
      context['count']=context['tasks'].filter(complete=False).count()
      search_input=self.request.GET.get('search-area') or ''
      if search_input:
         context['tasks']=context['tasks'].filter(title__startswith=search_input)
      context['search_input']=search_input
      return context
      
class TaskDetail(LoginRequiredMixin,DetailView):
   model = Task

class TaskCreate(LoginRequiredMixin,CreateView):
   model = Task
   fields=['title','description','complete']
   success_url=reverse_lazy('tasks')
   def form_valid(self, form):
      form.instance.user=self.request.user
      return super(TaskCreate,self).form_valid(form)
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="task"#by default it would be object2
    success_url=reverse_lazy('tasks')
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'tasks')
    else:
        form = FeedbackForm()
    return render(request, 'makin/feedback_form.html', {'form': form})
def pomodoro(request):
      return render(request,'makin/pomodoro.html')
def first(request):
      return render(request,'makin/first.html')
def non_acad(request):
      return render(request,'makin/non_acad.html')
def describe(request):
      return render(request,'makin/describe.html')     
def foundational(request):
      return render(request,'makin/foundational.html')
def secondary(request):
      return render(request,'makin/secondary.html')
def preparatory(request):
      return render(request,'makin/preparatory.html')
def middle(request):
      return render(request,'makin/middle.html')
def outdoor(request):
      return render(request,'makin/outdoor.html')
def  describe(request):
  return render(request,'makin/describe.html')
def deindactive(request):
  return render(request,'makin/deindactive.html')
def others(request):
  return render(request,'makin/others.html')
def indoor(request):
      return render(request,'makin/indoor.html')
def imag(request):
      return render(request,'makin/imag.html')
def alert(request):
      return render(request,'makin/alert.html')
def leisure(request):
      return render(request,'makin/leisure.html')