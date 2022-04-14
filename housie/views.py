from django.shortcuts import render
import random
# Create your views here.
    
def home(request):
    random_numbs=random.sample(range(1,91),90)
    request.session['recent_nums']=random_numbs
    recent_numbers= request.session['recent_nums']
    return render(request,"tambola/home.html",{'random':random_numbs, 'recent_numbers':recent_numbers})