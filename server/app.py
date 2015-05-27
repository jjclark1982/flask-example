import os
from flask import Flask, redirect, render_template, send_from_directory
if __package__:
    from . import database
else:
    import database

# This module is a Flask app, which can handle HTTP requests for a WSGI server
app = Flask(__name__.split('.')[0], static_folder=None)
app.debug = os.environ.get('DEBUG')

# We serve files from the nearby 'public' folder
app.template_folder = os.path.realpath(os.path.join(__file__,'..','..','public'))

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def serve_file(path):
    """Catch-all route handler"""

    # serve a folder
    if os.path.isdir(os.path.join(app.template_folder, path)):
        if path[-1] == '/':
            return serve_file(path + 'index.html')
        else:
            return redirect(path+'/')

    # serve a template file
    (basename, extname) = os.path.splitext(path)
    if extname.lower() == '.html':
        return render_template(path, db=database)

    # serve a static file
    else:
        return send_from_directory(app.template_folder, path)

# When running this file directly, print a site map
if __name__ == '__main__':
    print("Defined routes:")
    for rule in app.url_map.iter_rules():
        print("%s -> %s" % (rule.rule, rule.endpoint))
    for status in app.error_handlers:
        print("Error %s -> %s" % (status, app.error_handlers[status].__name__))
