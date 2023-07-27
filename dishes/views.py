from django.shortcuts import render, redirect
from .models import dish, User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def welcome(request):
    if request.method == 'POST':
        dish_name = request.POST['dish_name']
        dish_description = request.POST['dish_description']
        dish_image = request.FILES.get('dish_image')

        dish.objects.create(
            dish_name = dish_name,
            dish_description = dish_description,
            dish_image = dish_image
        )
        return redirect('welcome')
    queryset = dish.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(dish_name__icontains = request.GET.get('search'))

    context = {'dishes': queryset,'user':User}
    return render(request, 'welcome.html', context)
@login_required(login_url='/login/')
def update_dish(request, id):
    queryset = dish.objects.get(id = id)
    
    if request.method == "POST":
        dish_name = request.POST['dish_name']
        dish_description = request.POST['dish_description']
        dish_image = request.FILES.get('dish_image')

        queryset.dish_name = dish_name
        queryset.dish_description = dish_description

        if dish_image:
            queryset.dish_image = dish_image

        queryset.save() 
        return redirect('welcome')
    
    context = {'dishes': queryset}
    
    return render(request, 'update_dish.html', context)

def delete_dish(request, id):
    queryset = dish.objects.get(id = id)
    queryset.delete()
    return redirect('welcome')



