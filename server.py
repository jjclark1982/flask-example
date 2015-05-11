#!/usr/bin/env python

import os
from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__.split('.')[0], template_folder='public')
app.debug = ('DEBUG' in os.environ)

# General-purpose route handlers

@app.route('/')
def index():
    return serve_file('/index.html')

@app.route('/<path:path>')
def serve_file(path):
    # serve a directory
    if os.path.isdir(os.path.join('public', path)):
        if path[-1] == '/':
            return serve_file(path + '/index.html')
        else:
            return redirect(path+'/')

    # serve a template file
    basename, extname = os.path.splitext(path)
    if extname == '.html':
        return render_template(path)

    # serve a static file
    else:
        return send_from_directory('public', path)

# For running this file directly
if __name__ == '__main__':
    app.run()

# For running as a gunicorn worker
import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1
