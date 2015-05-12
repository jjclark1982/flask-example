# Example Flask + Jinja2 + SQLAlchemy app

This demonstrates the use of template-accessible Database and HTTP modules to achieve rapid foolproof deployment.

Compatible with most Platform-as-a-service providers.

### Installation

    pip install -r requirements.txt

### Configuration

    export DATABASE=postgresql+pypostgresql://username:password@host:port/database
    export WEB_CONCURRENCY=4
    export DEBUG=1

PROTIP: spin up a database

    DB_CONTAINER=$(docker run -e POSTGRES_PASSWORD=$(pwgen 12 1) -P -d postgres)
    docker inspect $DB_CONTAINER | grep 'POSTGRES_PASSWORD\|HostPort'

### Usage

    python server.py
