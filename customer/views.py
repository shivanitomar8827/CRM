from django.shortcuts import render, redirect

from .models import *

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework.response import Response




# Create your views here.




from .forms import NoteForm


def create_note_user(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            text_note = form.cleaned_data['text_note']
            call_type = form.cleaned_data['call_type']
            
            user = User.objects.get(username=user)
            
            UserNote.objects.create(user=user,text_note=text_note,call_type=call_type)
            
            return redirect('/customer/create_note')
    
    else:
        form = NoteForm()
    users = UserNote.objects.all().order_by('-user')
    return render(request, 'note.html', {'users':users,'form': form})


# all users list show
def user_list(request):


    users = User.objects.all()
    
    return render(request, 'users.html', {'users': users})  



def user_note_list(request):
    users = UserNote.objects.all().order_by('-user')
    return render(request, 'notelist.html', {'users': users})    




def delete_note(request, note_id):
    note = UserNote.objects.get(id=note_id)
    note.delete()
    return redirect('/customer/create_note')
    










    
        
