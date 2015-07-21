# Example Flask + Jinja2 + SQLAlchemy app

This demonstrates the use of template-accessible Database and HTTP modules to achieve rapid foolproof deployment.

Compatible with most Platform-as-a-service providers.

### Installation

Install Python 3 and `pip`. Use pip to install this project's dependencies:

    cd flask-example
    pip install -r requirements.txt

### Usage

    python server.py

### Configuration

Behavior is configured through environment variables. A typical development environment would look like this:

    export DATABASE_URL=sqlite:///data/development.db
    export WEB_CONCURRENCY=1
    export DEBUG=1
    export PORT=8000

If you store these in a file called `.env` (without "export"), they can be automatically set every time by `honcho`:

    honcho start
