FROM python:3.4

RUN pip install \
honcho==0.6.6 \
Flask==0.10.1 \
Jinja2==2.7.3 \
Markdown==2.6.2 \
MarkupSafe==0.23 \
PyYAML==3.11 \
SQLAlchemy==1.0.4 \
Werkzeug==0.10.4 \
gunicorn==19.3.0 \
itsdangerous==0.24 \
pg8000==1.10.2 \
python-frontmatter==0.2.1 \
six==1.9.0

WORKDIR /app/

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app/

ENV PORT 80
EXPOSE 80

CMD ["/usr/local/bin/honcho", "start"]
