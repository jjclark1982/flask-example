# Example Flask + Jinja2 + SQLAlchemy app

This demonstrates the use of template-accessible Database and HTTP modules to achieve rapid foolproof deployment.

Compatible with most Platform-as-a-service providers.

### Installation

Install Python 3 and `pip`. Globally install `virtualenv`:

    sudo pip install virtualenv

Locally install this project's dependencies:

    cd flask-example
    virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

### Configuration

Behavior is configured through environment variables. A typical development environment would look like this:

    export DATABASE_URL=sqlite:///data/development.db
    export WEB_CONCURRENCY=1
    export DEBUG=1
    export PORT=8000

### Usage

    python server
