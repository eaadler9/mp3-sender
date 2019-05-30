from pytube import YouTube

def downloadSong(YoutubeUrl, destination):
    yt = YouTube(YoutubeUrl)
    videos = yt.streams.all()

    s = 1
    for v in videos:
        print(str(s)+". "+str(v))
        s += 1

    vid = videos[0]

    vid.download(destination)
    print(vid);
