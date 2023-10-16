FROM --platform=$BUILDPLATFORM python:3.11.3 AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pipenv install --deploy --ignore-pipfile --system
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip install -U django-rest-knox
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]