from django.shortcuts import render
import datetime
# Create your views here.


def filter(request):
    context = {}
    context['character_list'] = ['a', 'b', 'c', 'd', 'e', 'f']
    context['single_int'] = 4
    context['sentence'] = 'My name is Noyon'
    context['word'] = 'hello'
    context['date'] = datetime.date.today
    context['list_of_dict'] = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context['small_alphabet_sentence'] = 'my name is noyon'
    today = datetime.date.today()
    context['one_year_previous_date'] = today - datetime.timedelta(days=366)
    context['filesize'] = 123847434947
    context['time'] = datetime.datetime.now()
    return render(request, 'filter.html', {'context': context})
