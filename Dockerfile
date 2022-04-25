FROM python:3.8

ENV PYTHONDONTTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /projects/choice

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
