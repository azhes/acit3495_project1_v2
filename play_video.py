import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from download_video import download_video
from write_to_mysql import write_to_mysql
from upload import upload_video_file

@app.route('/', methods=['GET', 'POST'])
def play_video():
    try:
        if request.form['play_video']:
            filename_no_prefix = request.form['play_video']
            filename = f'static/uploads/{filename_no_prefix}'
            filename = filename.replace('(', '')
            filename = filename.replace(')', '')
            filename = filename.replace(',', '')
            filename = filename.replace("'", '')
            download_video(filename)
            return render_template('play_video.html', filename=filename)
    except:
        if 'file' not in request.files:
            flash('No file part')
            return redirect('http://localhost:5001')
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect('http://localhost:5001')
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(f'Filename: {filename}')
            flash('Video successfully uploaded and displayed below')
            write_to_mysql(filename)
            upload_video_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('play_video.html', filename='static/uploads/' + filename)