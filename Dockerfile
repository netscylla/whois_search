FROM python:3.6.8-slim-stretch

RUN mkdir /opt/whois/
WORKDIR /opt/whois/
RUN echo "Installing whois"
COPY . .
RUN pip install -r requirements.txt
RUN echo "Done"
EXPOSE 5000/tcp
ENV FLASK_APP=app.py
CMD [ "flask","run","--host=0.0.0.0"]
USER nobody

