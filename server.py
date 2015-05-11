#!/usr/bin/env python

import os
from flask import Flask, render_template, send_from_directory, redirect
import multiprocessing
workers = multiprocessing.cpu_count()

app = Flask(__name__.split('.')[0], template_folder='public')
app.debug = ('DEBUG' in os.environ)

@app.route('/')
def index():
    return serve_file('/index.html')

@app.route('/<path:path>')
def serve_file(path):
    basename, extname = os.path.splitext(path)

    # serve a directory
    if os.path.isdir(os.path.join('public', path)):
        if path[-1] == '/':
            return send_from_directory('public', path + 'index.html')
        else:
            return redirect(path+'/')

    # serve a template file
    elif extname == '.html':
        return render_template(path)

    # serve a static file
    else:
        return send_from_directory('public', path)

if __name__ == '__main__':
    app.run()

