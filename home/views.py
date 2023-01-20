from django.shortcuts import render
from pytube import *
import os


def home(request):
    if request.method == 'POST':
        url = request.POST['link']
        if request.POST['download'] == 'Video':
            try:
                YouTube(url).streams.get_highest_resolution().download()
            except:
                return render(request, 'index.html')

        elif request.POST['download'] == 'Áudio':
            try: 
                out_file = YouTube(url).streams.get_audio_only().download()
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            except:
                return render(request, 'index.html')
        return render(request, 'concluido.html')     
    return render(request, 'index.html')