from urllib import response
from django.shortcuts import render
import requests

# Create your views here.

def exchange(request):
    response_val = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response_val.get('rates')
    
    if request.metod == 'GET':
        
        context = {
            'currencies':currencies,
        }
        
        return render(request, 'moneys_converter/index.html', context)
    
    if request.method == "POST":
        
        form_amount = float(request.POST.get('form-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(form_amount), 2)
        
        context = {
            "form_amount": form_amount,
            "from_curr": from_curr,
            "to_curr": to_curr,
            "converted_amount": converted_amount,
        }
        
        return render(request, 'moneys_converter/index.html', context)
    