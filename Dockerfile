FROM tiangolo/uvicorn-gunicorn-fastapi
COPY ./src/ /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt