from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'RAF Inventory',
        'name': 'Rafif Firmansyah Aulia',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)