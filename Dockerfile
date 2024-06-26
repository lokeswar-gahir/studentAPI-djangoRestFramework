FROM python:3.10.6-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY manage.py .
COPY ./core ./core
COPY ./home ./home

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
EXPOSE 8000
CMD [ "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000" ]
