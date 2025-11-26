from django.shortcuts import render
from advertisements.models import Advertisements

def Ad(request):
  advertisements = Advertisements.objects.all()
  return render(request = request, template_name = 'advertisements/index.html', context = {'advertisements': advertisements})
