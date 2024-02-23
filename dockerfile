FROM python:3.10.13
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .