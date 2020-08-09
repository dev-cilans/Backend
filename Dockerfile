FROM tiangolo/uvicorn-gunicorn-fastapi
RUN mkdir /app/test/
WORKDIR /app
RUN pip install -r requirements.txt
