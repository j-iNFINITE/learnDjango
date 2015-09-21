from django.shortcuts import render
from django.http import HttpResponse
from west.models import Character
# Create your views here.
def first_page(request):
    return HttpResponse('你妹')
def staff(request):
    staff_list = Character.objects.all()
    return render(request,'west.html', {'staffs': staff_list})

def templay(request):
    context = {}
    context['label'] = 'hehehehe'
    return render(request,'west.html',context)