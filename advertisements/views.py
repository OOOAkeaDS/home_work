from django.shortcuts import render, get_object_or_404, redirect
from advertisements.forms import AdForm
from advertisements.models import Advertisements

def Ad(request):
  advertisements = Advertisements.objects.all()
  return render(request = request, template_name = 'advertisements/index.html', context = {'advertisements': advertisements})

def get_ad_detail(request, ad_id):
   return render(request, 'advertisements/ads_detail.html', {"ad": get_object_or_404(Advertisements, id=ad_id)})

def create_ad(request):
  # form = AdForm(request.POST or None)
  form = AdForm()
  # if request.method == "POST":
  #   if form.is_valid():
  #     ad = Advertisements.objects.create(
  #       title=form.cleaned_data['title'],
  #       text=form.cleaned_data['text']
  #     )
  #     return redirect('ad_detail', ad_id=ad.id)
  return render(request, 'advertisements/ad_add.html', {"form": form})