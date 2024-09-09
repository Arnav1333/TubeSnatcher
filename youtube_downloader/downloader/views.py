import os
from django.shortcuts import render,redirect
from django.http import HttpResponse, StreamingHttpResponse
from pytube import YouTube
import tempfile
import os
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from pytube import YouTube
import tempfile
from .models import Download
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from .forms import RegisterForm

@login_required
def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url') 
        if url:
            try:
                yt = YouTube(url)
                video_stream = yt.streams.get_highest_resolution()
                temp_dir = tempfile.gettempdir()
                video_path = video_stream.download(output_path=temp_dir)
                file_name = f"{yt.title}.mp4" 
                response = HttpResponse(open(video_path, 'rb'), content_type='video/mp4') 
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'

                Download.objects.create(user=request.user, video_title=yt.title)

                response = HttpResponse(open(video_path, 'rb'), content_type='video/mp4') 
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                
                os.remove(video_path)
                return response
            
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}") 
            
    return render(request, 'downloader/download.html')

@login_required
def profile(request):
    downloads = Download.objects.filter(user=request.user)
    return render(request, 'profile.html', {'downloads': downloads})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('profile')  
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request,'home.html')