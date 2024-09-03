from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'fifthapp/input.html')

def add(request):
    a=request.GET['n1']
    b=request.GET['n2']
    c=int(a)+int(b)
    return render(request,'fifthapp/addition.html',{'c':c})