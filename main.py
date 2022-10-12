import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from upload import upload_video_file
from write_to_mysql import write_to_mysql
from create_tables import create_table
from get_videos import get_videos
from download_video import download_video



@app.route('/')
def upload_form():
    # if request.method == "POST":
    videos_list = get_videos()
    return render_template('upload.html', videos_list=videos_list)
    # elif request.method == "GET":
        # return redirect('http://localhost:5002/authenticate', 301)


@app.route('/', methods=['POST'])
def upload_video():
    try:
        if request.form['uname']:
            videos_list = get_videos()
            return render_template('upload.html', videos_list=videos_list)
    except:
        try:
            if request.form['play_video']:
                return redirect('http://localhost:5003', 307)
        except:
            return redirect('http://localhost:5003', 307)



# @app.route("/", methods=['POST'])
# def buttons():
#     videos_list = get_videos()
#     filename = request.form['play_video']
#     download_video(filename)
#     return render_template('upload.html', filename=filename, videos_list=videos_list)
            

# @app.route('/display/<filename>')
# def display_video(filename):
#     # print(f'Filename: {filename}')
#     return redirect(url_for('static', filename=filename), code=301)

if __name__ == '__main__':
    app.run()
