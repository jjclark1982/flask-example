# Example Flask + Jinja2 + SQLAlchemy app

This demonstrates the use of template-accessible Database and HTTP modules to achieve rapid foolproof deployment.

Compatible with most Platform-as-a-service providers.

### Installation

    pip install -r requirements.txt

### Configuration

    export DATABASE_URL=sqlite:///data/development.db
    export WEB_CONCURRENCY=1
    export DEBUG=1
    export PORT=8000

### Usage

    python server.py
