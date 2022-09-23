from django.shortcuts import render
from .forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)