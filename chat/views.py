from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'chat/index.html', {
        'name': request.user.username.upper()
    })

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'room_title': room_name.upper(),
        'name': request.user.username.upper()
    })