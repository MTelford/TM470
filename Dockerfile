FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    # Add other packages as needed
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY src /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt
RUN pygbag --build main.py

EXPOSE 8000

CMD ["python3", "WebServer.py"]
