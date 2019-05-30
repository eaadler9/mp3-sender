from flask import Flask, render_template, request
from pytube import YouTube
import YouTubeVideoDownloader

app = Flask(__name__)

nn = 'C:'+'\\'+'Users'+'\\'+'eaadl'+'\\'+'OneDrive'+'\\'+'Desktop'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html');

@app.route("/", methods=['POST'])
def about():
    name = request.form['name']
    email = request.form['email']
    song = request.form['song-sink']
    message = request.form['message']
    YouTubeVideoDownloader.downloadSong(song, nn);
    return render_template('about.html', n=name, e=email, s=song, m=message);


if __name__ == '__main__':
    app.debug = True
    app.run()
