import os
from app import app
import urllib.request
import json
from flask import Flask, flash, request, redirect, url_for, render_template

@app.route('/authenticate', methods=['GET'])
def show_form():
    return render_template('authenticate.html')
        

@app.route('/authenticate', methods=['POST'])
def authenticate():
    with open('users.json', 'r') as f:
            data = json.load(f)
    username = request.form['uname']
    password = request.form['psw']
    usernames = []
    passwords = []
    for user in data:
        uname = data[user]['username']
        passw = data[user]['password']
        usernames.append(uname)
        passwords.append(passw)

    if username in usernames and password in passwords:
        return redirect('http://localhost:5001', 307)
    else:
        return render_template('authenticate.html')

if __name__ == '__main__':
    app.run(port=5002)