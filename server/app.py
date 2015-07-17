import os
from flask import Flask, Markup, redirect, render_template, send_from_directory
import markdown
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
    full_path = os.path.join(app.template_folder, path)
    (basename, extname) = os.path.splitext(path)

    # serve a folder
    if os.path.isdir(full_path):
        if path[-1] == '/':
            return serve_file(path + 'index.html')
        else:
            return redirect(path+'/')

    # serve a jinja2 file
    if extname.lower() == '.html':
        return render_template(path, db=database)

    # serve a markdown file
    if extname.lower() == '.md':
        f = open(full_path)
        content = Markup(markdown.markdown(f.read()))
        return Markup(content)

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
