from python:3.9-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]
