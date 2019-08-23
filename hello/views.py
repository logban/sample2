from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.shortcuts import redirect
from .forms import HelloForm




def index(request):
    data=Friend.objects.all()
    params = {
            'title':'Hello',
            'data':data,
            'goto':'create',
            }
    return render(request, 'hello/index.html', params)


#create model
def create(request):
    params={
            'title':'Hello',
            'form':HelloForm(),
            'goto':'index',
            }
    if (request.method == "POST"):
        name = request.POST['name']
        mail = request.POST['mail']
        gender='gender' in request.POST
        age = int(request.POST['age'])
        friend = Friend(name = name, mail = mail, gender=gender,\
                        age= age)
        friend.save()
        return redirect(to='/hello/hanei')
    return render(request, 'hello/create.html',params)

def hanei(request):
    data=Friend.objects.all()
    da = Friend.objects.all().count()
    params={
            'da':da,
            'title':'Hello',
            'data':data,
            'goto':'index',
            }
    return render(request, 'hello/hanei.html',params)

