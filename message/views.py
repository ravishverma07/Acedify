from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Message, Profile

def user_list(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')  # Adjust as per your login URL
    profiles = Profile.objects.all()
    print("profiles : ",profiles)
    return render(request, 'messages/user_list.html', {'profiles': profiles})

# @login_required
def chat(request, username):
    user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(
        sender=request.user, receiver=user
    ) | Message.objects.filter(
        sender=user, receiver=request.user
    )
    if request.method == "POST":
        content = request.POST.get('content')
        Message.objects.create(sender=request.user, receiver=user, content=content)
        return redirect('chat', username=user.username)

    return render(request, 'messages/chat.html', {'messages': messages, 'receiver': user})
