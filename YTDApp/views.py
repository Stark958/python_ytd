from django.shortcuts import render, redirect
# pytube package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
import pafy


def ytb_down(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        bestvideo = video.getbest()
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'bestobj':bestvideo,
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'YTDApp/hi.html', context)
    return render(request, 'YTDApp/hi.html')
