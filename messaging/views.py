from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Message


User = get_user_model()


@login_required
def conversation(request, user_id):

    other_user = get_object_or_404(
        User,
        id=user_id
    )

    messages = Message.objects.filter(
        sender=request.user,
        receiver=other_user
    ) | Message.objects.filter(
        sender=other_user,
        receiver=request.user
    )

    messages = messages.order_by('sent_at')

    Message.objects.filter(
        sender=other_user,
        receiver=request.user,
        is_read=False
    ).update(
        is_read=True
    )

    if request.method == 'POST':

        message_text = request.POST.get(
            'message',
            ''
        ).strip()

        if message_text:

            Message.objects.create(
                sender=request.user,
                receiver=other_user,
                message=message_text
            )

        return redirect(
            'conversation',
            user_id=other_user.id
        )

    context = {
        'other_user': other_user,
        'messages': messages,
    }

    return render(
        request,
        'messaging/conversation.html',
        context
    )


# =====================================
# TEACHER INBOX
# =====================================

@login_required
def inbox(request):

    received_messages = Message.objects.filter(
        receiver=request.user
    ).select_related(
        'sender'
    ).order_by('-sent_at')

    unread_count = Message.objects.filter(
        receiver=request.user,
        is_read=False
    ).count()

    context = {
        'received_messages': received_messages,
        'unread_count': unread_count,
    }

    return render(
        request,
        'messaging/inbox.html',
        context
    )