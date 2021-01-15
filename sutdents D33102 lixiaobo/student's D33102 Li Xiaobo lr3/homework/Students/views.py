from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from .models import tercher,performance,discipline,homework,student

def discipline_list(response):
    di=discipline
    dis= discipline.objects.all()
    L=discipline.objects.get(pk=1)
    M=discipline.objects.get(pk=2)
    P=discipline.objects.get(pk=3)
    Lts=L.tercher_set.all()
    Mts=M.tercher_set.all()
    Pts=P.tercher_set.all()
    return render(response, "discipline_list.html" ,context=locals())

def homeworke_data(response,id_dis):
    dis=discipline.objects.get(pk=id_dis)
    hs=dis.homework_set.all()
    cont={"di":dis,"hs":hs}
    return render(response,"homework_data.html", context=cont)
class hwUpdateView(UpdateView):
  model = homework
  fields = ["execution_period", "task_text", "date_issue","penalty", "id_discipline"]
  success_url ="/HW/dis_list/"
  template_name = 'homework_Updata.html'

class student_list(ListView):
    model = student
    template_name = "student_list.html"

class student_data(DetailView):
        model = student
        template_name = "student_data.html"
class pUpdateView(UpdateView):
  model = performance
  fields = ["score", "Completion_date", "id_homeworke","id_student"]
  success_url ="/HW/dis_list/"
  template_name = 'p_Updata.html'
def base(response):
    return render(response, 'base.html')
class create_hw(CreateView):
        model = homework
        fields = ['execution_period','task_text','date_issue','penalty','id_discipline']
        template_name = "set_homewk.html"


class add_hw(CreateView):
    model = performance
    fields = ['id_homeworke', 'id_student']
    template_name = "sad_homewk.html"
    success_url = "/HW/student_list/"

def delete_hw(request,pk):
    p=performance.objects.get(pk=pk)
    p.delete()
    return HttpResponseRedirect("/HW/student_list/")
def delete_HW(request,pk):
    p=homework.objects.get(pk=pk)
    p.delete()
    return HttpResponseRedirect("/HW/dis_list/")


