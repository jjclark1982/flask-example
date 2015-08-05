FROM python:3.4

RUN pip install honcho

WORKDIR /app/

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app/

ENV PORT 80
EXPOSE 80

CMD ["/usr/local/bin/honcho", "start"]
