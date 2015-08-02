#!/usr/bin/env python

import os
from flask import Flask, Markup, redirect, render_template, send_from_directory
import markdown
import database

# This module is a Flask app, which can handle HTTP requests for a WSGI server
app = Flask(__name__.split('.')[0], static_folder=None)
app.debug = os.environ.get('DEBUG')

# We serve files from the nearby 'public' folder
app.template_folder = os.path.realpath(os.path.join(__file__,'..','public'))

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def serve_file(path):
    """Catch-all route handler"""
    full_path = os.path.join(app.template_folder, path)
    (basename, extname) = os.path.splitext(path)

    # serve a folder
    if os.path.isdir(full_path):
        if path[-1] == '/':
            return serve_file(path + 'index.html')
        else:
            return redirect(path+'/')

    # serve a jinja2 file
    elif extname.lower() == '.j2':
        return render_template(path, db=database)

    # serve a markdown file
    elif extname.lower() == '.md':
        f = open(full_path)
        content = Markup(markdown.markdown(f.read()))
        return Markup(content)

    # serve a static file
    else:
        return send_from_directory(app.template_folder, path[1:])

# When running this file directly, start a server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT') or 8000))
