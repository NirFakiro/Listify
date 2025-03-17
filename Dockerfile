FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir mysql-connector-python pandas -r requirements.txt
COPY . .
COPY ./public /app/static
EXPOSE 5000
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
CMD ["flask","run"]
