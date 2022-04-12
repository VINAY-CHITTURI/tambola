from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
# Create your views here.
def access_ses(request):
    del request.session['recent_nums']
    return HttpResponse('session delete hogaya re hawle')

def numbers(request):
    random_numb=random.randint(1,90)
    request.session['recent_nums']=random_numb
    return request.session['recent_nums']
    
def home(request):
    random_numbs=random.sample(range(1,91),90)
    #if 'recent_nums' in request.session:
    request.session['recent_nums']=random_numbs
    recent_numbers= request.session['recent_nums']
    return render(request, 'tambola/home.html',{'random':random_numbs, 'recent_numbers':recent_numbers})


def get_response(request):
    user_input = request.GET.get('inputValue')
    data = {'response': f'You typed: {user_input}'}
    return JsonResponse(data)