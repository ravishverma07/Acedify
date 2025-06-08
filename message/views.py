from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Message, Profile
from  users.models import CustomUser

@login_required
def user_list(request):
    current_user = request.user  # Get the logged-in user
    semester_choices = CustomUser._meta.get_field('semester').choices  # Fetch semester choices

    if request.method == "POST":
        semester = request.POST.get('semester')
        if semester:
            current_user.semester = semester
            current_user.save()
            messages.success(request, "Semester updated successfully!")

    # Fetch all profiles excluding the current user
    profiles = CustomUser.objects.exclude(id=current_user.id)

    # Add a 'new_messages_count' attribute to each profile
    for profile in profiles:
        profile.new_messages_count = Message.objects.filter(
            sender=profile, 
            receiver=current_user, 
            is_read=False
        ).count()

    return render(
        request, 
        'messages/user_list.html', 
        {
            'profiles': profiles, 
            'current_user': current_user, 
            'semester_choices': semester_choices
        }
    )


@login_required
def chat(request, username):
    other_user = get_object_or_404(CustomUser, username=username)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')

    # Mark messages as read
    messages.filter(receiver=request.user, is_read=False).update(is_read=True)

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=other_user, content=content)

    return render(request, 'messages/chat.html', {'messages': messages, 'receiver': other_user})
