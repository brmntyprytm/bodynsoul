from django.shortcuts import render, redirect
from .models import Mood
from .forms import MoodForm

def mood_list(request):
    moods = Mood.objects.all()
    return render(request, 'mood/mood_list.html', {'moods': moods})

def mood_create(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mood_list')
    else:
        form = MoodForm()
    return render(request, 'mood/mood_form.html', {'form': form})

def mood_links(request, mood_name):
    mood_links = {
        "happy": "https://www.happier.com",
        "sad": "https://www.verywellmind.com/how-to-cope-with-sadness-3145105",
        "anxious": "https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm",
        "angry": "https://www.apa.org/topics/anger/control",
        "relaxed": "https://www.mindful.org/meditation/mindfulness-getting-started/",
        # Add more moods and corresponding links as needed
    }
    link = mood_links.get(mood_name.lower(), "No link available for this mood")
    return render(request, 'mood/mood_links.html', {'mood': mood_name, 'link': link})
