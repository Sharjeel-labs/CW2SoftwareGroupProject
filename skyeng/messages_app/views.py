from django.shortcuts import render, redirect
from .models import Message


def inbox(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'messages_app/inbox.html', {'messages': messages})


def compose(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        Message.objects.create(
            sender="testuser",   # simple placeholder
            receiver=receiver,
            subject=subject,
            body=body,
            is_draft=False
        )

        return redirect('inbox')

    return render(request, 'messages_app/compose.html')


def sent(request):
    messages = Message.objects.filter(sender="testuser").order_by('-created_at')
    return render(request, 'messages_app/sent.html', {'messages': messages})


def drafts(request):
    messages = Message.objects.filter(is_draft=True).order_by('-created_at')
    return render(request, 'messages_app/drafts.html', {'messages': messages})


def trash(request):
    return render(request, 'messages_app/trash.html')