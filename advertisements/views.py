from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from advertisements.forms import AdForm
from advertisements.models import Advertisements, Category

def Ad(request):
  advertisements = Advertisements.objects.all()
  category = Category.objects.all()
  context = {'advertisements': advertisements,
             'category': category}
  return render(request = request, template_name = 'advertisements/index.html', context = context)

def get_ad_detail(request, ad_id):
   return render(request, 'advertisements/ads_detail.html', {"ad": get_object_or_404(Advertisements, id=ad_id)})

def create_ad(request):
  form = AdForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      ad = Advertisements.objects.create(
        title=form.cleaned_data['title'],
        text=form.cleaned_data['text'],
        category=form.cleaned_data['category']
      )
      return redirect('ad_detail', ad_id=ad.id)
  return render(request, 'advertisements/ad_add.html', {"form": form})