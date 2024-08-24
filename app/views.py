from django.shortcuts import render
def jinja_print(request):
    d={'name':'preeti','age':23}
    return render(request,'jinja_print.html',context=d)

# Create your views here.
