from django.shortcuts import render
from django.http import HttpResponse
from west.models import Character
from django.core.context_processors import csrf
from django import forms
# Create your views here.
def first_page(request):
    return HttpResponse(print(request.user.is_authenticated))
def staff(request):
    staff_list = Character.objects.all()
    return render(request,'west.html', {'staffs': staff_list})

def templay(request):
    context = {}
    context['label'] = 'hehehehe'
    return render(request,'west.html',context)

def form(request):
    return render(request, 'form.html')
class CharacterForm(forms.Form):
    name = forms.CharField(max_length=200)
def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted = request.POST['name']
            new_record = Character(name=submitted)
            new_record.save()
    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['form']=form
    ctx['staff'] = all_records
    return render(request,'investigate.html',ctx)
