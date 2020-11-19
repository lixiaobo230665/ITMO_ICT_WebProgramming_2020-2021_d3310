from django.http import Http404
from django.shortcuts import render
from .models import driver,Car,Ownership
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def detail(request, driver_id):
    try:
        dr = driver.objects.get(pk=driver_id)
    except driver.DoesNotExist:
        raise Http404("driver does not exist")
    return render(request, 'driver.html', {'driver': dr})

class driver_list(ListView):
    model = Ownership
    template_name = "driver_list.html"

class driver_deta(DetailView):
    model = Ownership
    template_name = "driver_data.html"

class Car_deta(DetailView):
    model = Car
    template_name = "Car_deta.html"
def delete_driver_deta(respons,pk):
    d = driver.objects.get(pk=pk)
    d.delete()
    return render(respons, 'delete_driver_deta.html')
from .forms import FACForm
def create_view(request):
    context = {}
    form = FACForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_Car.html", context)
def delete_Car_data(respons,pk):
    c = Car.objects.get(pk=pk)
    c.delete()
    return render(respons, 'delete_Car_data.html')
from django.views.generic.edit import UpdateView
class Update_Car(UpdateView):
    model = Car
    fields = ['state_number', 'Colour', 'Brand', 'Car_type']
    success_url = '/driver_list/'
    template_name = 'update_Car.html'

