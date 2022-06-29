from django.shortcuts import render

# Create your views here.

def exchange(request):
    name = 'mr. Anderson'
    
    context = {
        'name': name
    }
    
    return render(request, 'moneys_converter/index.html', context)