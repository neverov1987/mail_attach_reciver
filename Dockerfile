FROM python:3.9-alpine
COPY main.py .
COPY requirements.txt .
RUN apk add curl \
    && \
    pip install -r requirements.txt
CMD python3 main.py
