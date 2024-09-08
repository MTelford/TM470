FROM python:3.12

WORKDIR /app

COPY src /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pygbag --build main.py

EXPOSE 80

ENV NAME JackChangeIt

CMD ["python3", "WebServer.py"]
