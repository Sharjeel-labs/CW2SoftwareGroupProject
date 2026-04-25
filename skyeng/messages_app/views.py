from django.shortcuts import render

def inbox(request):
    return render(request, 'messages_app/inbox.html')

def compose(request):
    return render(request, 'messages_app/compose.html')

def sent(request):
    return render(request, 'messages_app/sent.html')

def drafts(request):
    return render(request, 'messages_app/drafts.html')

def trash(request):
    return render(request, 'messages_app/trash.html')