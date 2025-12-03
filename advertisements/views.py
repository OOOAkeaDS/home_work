from django.shortcuts import render, get_object_or_404
from advertisements.models import Advertisements

def Ad(request):
  advertisements = Advertisements.objects.all()
  return render(request = request, template_name = 'advertisements/index.html', context = {'advertisements': advertisements})

def get_ad_detail(request, ad_id):
  # return render(request, 'blog/post_detail.html', {"post": Post.objects.get(id=post_id)})
  return render(request, 'blog/post_detail.html', {"post": get_object_or_404(Post, id=ad_id)})

def create_ad(request):
  return render(request = request, template_name = 'advertisements/new_ad.html')