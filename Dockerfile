FROM tiangolo/uvicorn-gunicorn-fastapi
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
