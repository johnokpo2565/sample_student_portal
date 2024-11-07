from django.shortcuts import render, redirect
from .models import User
from .form import ProfilePicsForm

# Create your views here.

def home(request):
    user = User.objects.get(email = request.user)
    print(user.id)
    return render(request, 'account/dashboard.html', {
        'user':user
    })

def profile(request, pk):
    user = User.objects.filter(email=request.user).get(pk=pk)
    
    if request.method == "POST":
        form = ProfilePicsForm(request.POST, request.FILES)
        if form.is_valid():
            profilepics = form.save(commit=False)
            profilepics.user = user
            profilepics.save()

            return redirect("/account/")

    else:
        form = ProfilePicsForm()
    return render(request,'account/xc.html', {
        'form':form,
    })


def update_profile(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        address = request.POST.get('address','')
        age = request.POST.get('age', '')

        if age and address:
            user.address = address
            user.age = age
            user.save()
            return redirect("/account/")
        
    return render(request,'account/profile.html',{
        'user':user
    })