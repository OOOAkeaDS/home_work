from unicodedata import category
from django import forms
from .models import Category

class AdForm(forms.Form):
  title = forms.CharField(max_length=200, label="Заголовок объявления:", required=False,
    widget=forms.TextInput(attrs={
      'placeholder': "заголовок (максимальная длина 200 символов)"
    })
  )

  text = forms.CharField(label="Содержимое объявления:",
    widget=forms.Textarea(attrs={
      'row': 3
    })
  )
  
  category = forms.ModelChoiceField(queryset=Category.objects.all(), 
    empty_label="Выберите категорию",
    label="Категория",
    widget=forms.Select(attrs={'class': "form-control"
    })
  )
  
  isActive = True

  def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if not title:
      raise forms.ValidationError("Заголовок обязателен.")
    
    if len(title) < 5:
      raise forms.ValidationError("Заголовок не должен быть короче 5 символов.")
    
    return title
  