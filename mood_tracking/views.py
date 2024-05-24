from django.shortcuts import render, redirect
from main.models import Mood
from main.forms import MoodForm

def mood_tracking(request):
    if request.method == 'POST':
        form = MoodForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('mood_tracking:mood_tracking')
    else:
        form = MoodForm()

    moods = Mood.objects.filter(user=request.user)
    context = {'form': form, 'moods': moods}
    return render(request, 'mood_tracking.html', context)