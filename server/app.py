#!/usr/bin/env python3
import os

from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    # Get client info from request
    ip = request.remote_addr
    browser = request.headers.get('User-Agent', 'Unknown')
    
    # Create a response
    response = make_response(
        f"<h1>Welcome</h1>"
        f"<p>Your IP: {ip}</p>"
        f"<p>Browser: {browser}</p>"
    )
    
    # Set a cookie
    response.set_cookie('visited', 'yes')
    
    return response

@app.route('/secret')
def secret():
    if request.cookies.get('visited') != 'yes':
        abort(403)  # Forbidden if they haven't visited home
    return "You found the secret page!"

@app.route('/go-home')
def go_home():
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5555, debug=True)