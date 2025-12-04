
from django.db import models

class Category(models.Model):
  title = models.CharField(max_length=50, verbose_name="Категория")
  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    
  def __str__(self):
    return self.title
class Advertisements(models.Model):
  title = models.CharField(max_length=100, verbose_name="Заголовок")
  text = models.TextField(verbose_name="Текст")
  created_at = models.DateTimeField(auto_now_add=True)
  isActive = models.BooleanField(default=False, verbose_name="Объявление активно")
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

  class Meta:
    verbose_name = 'Объявление'
    verbose_name_plural = 'Объявления'

  def __str__(self):
    return self.title