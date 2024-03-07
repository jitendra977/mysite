from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    peoples = [
    {'fname': 'John', 'lname': 'Doe', 'age': 25},
    {'fname': 'Jane', 'lname': 'Doe', 'age': 30},
    {'fname': 'Michael', 'lname': 'Smith', 'age': 40},
   
]

    return render(request,'base.html',context={'peoples':peoples})

