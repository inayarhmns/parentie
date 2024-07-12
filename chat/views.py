from django.contrib.auth.decorators import login_required
from django.shortcuts import render



# Create your views here.
from .models import Thread
from authentication.models import User
from django.shortcuts import render, get_object_or_404


@login_required
def messages_page(request, thread_id=None):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    
    if thread_id:
        try:
            active_thread = get_object_or_404(Thread, id=thread_id)
        except Thread.DoesNotExist:
            active_thread = None
    else:
        active_thread = threads.first()
    
    context = {
        'threads': threads,
        'active_thread': active_thread,
    }
    return render(request, 'messages.html', context)

