import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from upload import upload_video_file
from write_to_mysql import write_to_mysql
from create_tables import create_table
from get_videos import get_videos

create_table()

@app.route('/', methods=["GET", "POST"])
def upload_form():
    if request.method == "POST":
        videos_list = get_videos()
        return render_template('upload.html', videos_list=videos_list)
    elif request.method == "GET":
        return redirect('http://localhost:5002/authenticate', 301)


@app.route('/', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print(f'Filename: {filename}')
        flash('Video successfully uploaded and displayed below')
        write_to_mysql(filename)
        upload_video_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        videos_list = get_videos()
        return render_template('upload.html', filename=filename, videos_list=videos_list)

@app.route("/", methods=['POST'])
def buttons():
    videos_list = get_videos()
    if request.method == 'POST':
        print(request.form['video'])
    
    return render_template('upload.html', filename=request.form['video'], videos_list=videos_list)
            

@app.route('/display/<filename>')
def display_video(filename):
    # print(f'Filename: {filename}')
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run()
