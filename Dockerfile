FROM tiangolo/uvicorn-gunicorn-fastapi
RUN mkdir /app/test/
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
