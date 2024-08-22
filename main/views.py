from django.shortcuts import render
from main.models import Columns, Cards

def index(request):

    columns = Columns.objects.all()
    list_columns = []

    for column in columns:
        list_columns.append({
            'title': column.name, 
            'cards': Cards.objects.filter(column=column),
        },)
    
    context = {
        'columns': list_columns
    }

    return render(request, 'main/index.html', context=context)


def card(request, card_slug):
    
    return render(request, 'main/card.html')