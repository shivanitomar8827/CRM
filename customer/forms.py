from django import forms
from .models import UserNote,CALL_CHOICES
from django.contrib.auth.models import User








class NoteForm(forms.Form):
    user = forms.ModelChoiceField(queryset= User.objects.all())
    text_note= forms.CharField(widget=forms.Textarea(attrs={"rows":"10"}))
    call_type= forms.ChoiceField(choices=CALL_CHOICES,widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}))  
    
    

# class UserNoteForm(forms.ModelForm):
#     class Meta:
#         model = UserNote
#         fields = ['code', 'text_note']