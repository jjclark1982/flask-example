# Example Flask + Jinja2 + SQLAlchemy app

This demonstrates the use of template-accessible Database and HTTP modules to achieve rapid foolproof deployment.

Compatible with most Platform-as-a-service providers.

# Installation

    pip install -r requirements.txt

# Configuration

    export DATABASE=postgresql+pypostgresql://username:password@host:port/database
    export DEBUG=1
    export WEB_CONCURRENCY=4

# Usage

    python server.py
