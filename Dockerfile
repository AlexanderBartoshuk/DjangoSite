FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/ 

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY Site /app/

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]