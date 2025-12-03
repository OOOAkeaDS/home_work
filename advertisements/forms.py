from django import forms

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

  def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if not title:
      raise forms.ValidationError("Заголовок обязателен.")
    
    if len(title) < 5:
      raise forms.ValidationError("Заголовок не должен быть короче 5 символов.")
    
    return title