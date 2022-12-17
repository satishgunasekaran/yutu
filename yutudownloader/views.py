from django.shortcuts import render
from pytube import YouTube
import os
# Create your views here.

url =""
def index(request):
    return render(request, 'index.html')

def download(request):
    if request.method == "GET":
        global url 
        url= request.GET.get('url')
        print("URL" ,url)
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True).all()
        print(video)

        embed_link = url.replace("watch?v=","embed/")
        title = yt.title
        context = {'video': video, 'embed' : embed_link, 'title':title}

        return render(request, 'download.html', context)

def yt_download_done(request, resolution):
    global url 
    homedir = os.path.expanduser("~")
    dirs = homedir +"/Downloads"
    if request.method == "POST":
        try:
            print("URL :",url)
            if resolution == "144p":
                print( YouTube(url).streams.get_by_itag(17))
                YouTube(url).streams.get_by_itag(17).download(dirs)
                return render(request, 'done.html')

            YouTube(url).streams.get_by_resolution(resolution).download(dirs)
            return render(request, 'done.html')
        except Exception as e:
            print(e)
            return render(request, "error.html")

    return render(request, "error.html")
