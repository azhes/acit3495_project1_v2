import os
from app import app
import urllib.request
import json
from flask import Flask, flash, request, redirect, url_for, render_template
from create_tables import create_table

@app.route('/authenticate', methods=['GET'])
def show_form():
    create_table()
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
        flash('Authentication failed')
        return render_template('authenticate.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        with open('users.json', 'r') as f:
            data = json.load(f)
        user_ids = data.keys()
        int_user_ids = []
        for id in user_ids:
            int_user_ids.append(int(id))
        new_user = max(int_user_ids) + 1
        data[new_user] = {"username": username, "password": password}
        json_string = json.dumps(data)
        with open('users.json', 'w') as f:
            f.write(json_string)
        flash('New user created. Please log in.')
        return render_template('authenticate.html')

if __name__ == '__main__':
    app.run(port=5002)